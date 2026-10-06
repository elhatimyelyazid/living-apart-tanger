import numpy as np, math, random
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops
random.seed(7); np.random.seed(7)
W,H=1080,1350
IMG='/tmp/claude-0/-home-user-living-apart-tanger/ed11bdfe-6371-5a48-a918-5a5849a11a36/images/1.jpg'

# ---- fabric
def lowfreq(sx,sy,amp):
    a=np.random.rand(sy,sx).astype('f4')
    return np.asarray(Image.fromarray((a*255).astype('u1')).resize((W,H),Image.BICUBIC),dtype='f4')/255*amp
yy,xx=np.mgrid[0:H,0:W]
weave=(np.sin(xx*2*math.pi/5)*np.sin(yy*2*math.pi/5))*5 + np.sin(xx*2*math.pi/11+np.sin(yy/30.))*3
noise=np.random.randn(H,W)*7
base=40+weave+noise+lowfreq(12,15,18)
light=1.25-0.75*(xx/W)           # hard side light from left
light=light*(1-0.25*(yy/H))
f=np.clip(base*light,0,255)
fabric=np.stack([f*1.0,f*1.02,f*1.08],-1).astype('u1')
fabric=Image.fromarray(fabric).convert('RGBA')

# ---- hair helpers
def bez(p0,p1,p2,n=14):
    return [((1-t)**2*p0[0]+2*(1-t)*t*p1[0]+t*t*p2[0],(1-t)**2*p0[1]+2*(1-t)*t*p1[1]+t*t*p2[1]) for t in [i/(n-1) for i in range(n)]]
def hcol(a=None):
    r=random.random()
    a=random.randint(120,235)
    if r<.5: return (236,226,208,a)
    if r<.8: return (214,196,168,a)
    return (246,242,232,a)
def strand(d,cx,cy,L,ang,curl=.35,w=None):
    dx,dy=math.cos(ang)*L,math.sin(ang)*L
    p0=(cx,cy); p2=(cx+dx,cy+dy)
    nx,ny=-dy*curl*random.uniform(-1,1),dx*curl*random.uniform(-1,1)
    p1=(cx+dx/2+nx,cy+dy/2+ny)
    d.line(bez(p0,p1,p2),fill=hcol(),width=w or random.choice([1,1,1,1,2]),joint='curve')

# ---- hair layer: everywhere except clean lane
hair=Image.new('RGBA',(W,H),(0,0,0,0)); hd=ImageDraw.Draw(hair)
LANE_X0,LANE_X1=440,970   # clean lane width = blade width
BLADE_Y=820
for i in range(21000):
    x=random.uniform(-40,W+40); y=random.uniform(-40,H+40)
    if LANE_X0<x<LANE_X1 and y<BLADE_Y: 
        # crisp lane edge: no strands starting inside lane
        continue
    strand(hd,x,y,random.uniform(30,120),random.uniform(0,2*math.pi))
# trim strands crossing into lane: mask the lane
mask=Image.new('L',(W,H),255); ImageDraw.Draw(mask).rectangle([LANE_X0,0,LANE_X1,BLADE_Y],fill=0)
hair.putalpha(ImageChops.multiply(hair.split()[3],mask))

# ---- ball of hair in front of blade (below blade, centered)
ball=Image.new('RGBA',(W,H),(0,0,0,0)); bd=ImageDraw.Draw(ball)
bx,by,br=705,BLADE_Y+85,150
for i in range(4200):
    a=random.uniform(0,2*math.pi); r=br*math.sqrt(random.random())
    x=bx+r*math.cos(a); y=by+r*0.78*math.sin(a)
    ang=a+math.pi/2+random.uniform(-1.2,1.2)
    L=random.uniform(40,160)
    strand(bd,x,y,L,ang,curl=.7)
# clip to ellipse-ish blob with noisy edge, keep a few flyaways
blob=Image.new('L',(W,H),0); ImageDraw.Draw(blob).ellipse([bx-br*1.02,by-br*.82,bx+br*1.02,by+br*.82],fill=255)
blob=blob.filter(ImageFilter.GaussianBlur(10))
fl=Image.new('RGBA',(W,H),(0,0,0,0)); fd=ImageDraw.Draw(fl)
for i in range(260):
    a=random.uniform(0,2*math.pi); strand(fd,bx+br*.9*math.cos(a),by+br*.7*math.sin(a),random.uniform(30,110),a+random.uniform(-.8,.8),.5,1)
ball.putalpha(ImageChops.multiply(ball.split()[3],blob))
ball=Image.alpha_composite(ball,fl)
# shading of the ball (lit from left, dark core between strands)
bn=np.asarray(ball,dtype='f4').copy()
sh=np.clip(1.15-0.55*((xx-(bx-br))/(2*br)),0.55,1.15)*np.clip(1.1-0.35*((yy-(by-br))/(2*br)),0.6,1.1)
bn[...,:3]*=sh[...,None]; ball=Image.fromarray(np.clip(bn,0,255).astype('u1'))

# shading for hair layer + shadows
hn=np.asarray(hair,dtype='f4').copy(); hn[...,:3]*=np.clip(light*0.85,0.5,1.15)[...,None]
hair=Image.fromarray(np.clip(hn,0,255).astype('u1'))
def shadow(layer,off=(5,7),blur=4,op=170):
    a=layer.split()[3].point(lambda v:v*op//255)
    s=Image.new('RGBA',(W,H),(0,0,0,0)); s.putalpha(ImageChops.offset(a,*off).filter(ImageFilter.GaussianBlur(blur))); return s
scene=fabric.copy()
scene=Image.alpha_composite(scene,shadow(hair))
scene=Image.alpha_composite(scene,hair)
scene=Image.alpha_composite(scene,shadow(ball,(14,18),12,210))
scene=Image.alpha_composite(scene,ball)

# ---- product cutout (exact photo)
im=Image.open(IMG).convert('RGB'); a=np.asarray(im,dtype='f4')
mn=a.min(-1); alpha=np.clip((250-mn)/(250-228),0,1)*255
al=Image.fromarray(alpha.astype('u1')).filter(ImageFilter.MinFilter(3))
prod=im.convert('RGBA'); prod.putalpha(al)
ANG=31.0; SC=0.44
prod=prod.rotate(ANG,expand=True,resample=Image.BICUBIC)
prod=prod.resize((int(prod.width*SC),int(prod.height*SC)),Image.LANCZOS)
# locate blade: place so that blade centre lands at (540,BLADE_Y)
# blade centre in original ~ (560,860) -> rotate about image centre
cx0,cy0=im.width/2,im.height/2
bxo,byo=560-cx0,860-cy0
r=math.radians(ANG)
rx=bxo*math.cos(r)+byo*math.sin(r); ry=-bxo*math.sin(r)+byo*math.cos(r)
px=int(705-(prod.width/2+rx*SC)); py=int(BLADE_Y-(prod.height/2+ry*SC))
layer=Image.new('RGBA',(W,H),(0,0,0,0)); layer.paste(prod,(px,py),prod)
scene=Image.alpha_composite(scene,shadow(layer,(16,20),14,200))
scene=Image.alpha_composite(scene,layer)

# ---- vignette / zones sombres
g=np.ones((H,W),'f4')
g*=np.clip(0.35+ (yy/330.),0,1)*0+1
top=np.clip(1-(yy/620.),0,1)**1.4*0.78
bot=np.clip((yy-960)/300.,0,1)**1.2*0.85
dark=np.clip(top+bot,0,0.92)
sc=np.asarray(scene.convert('RGB'),dtype='f4')*(1-dark[...,None])
sc=sc*(1-0.30*np.clip((np.hypot((xx-W/2)/W,(yy-H/2)/H)-0.35)/0.4,0,1))[...,None]
img=Image.fromarray(np.clip(sc,0,255).astype('u1')).convert('RGB')

# ---- text
d=ImageDraw.Draw(img)
SER='/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf'
SERI='/usr/share/fonts/truetype/liberation/LiberationSerif-BoldItalic.ttf'
SERR='/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf'
F1=ImageFont.truetype(SER,124); F2=ImageFont.truetype(SERI,124)
d.text((64,185),"TON CANAPÉ.",font=F1,fill=(255,255,255))
d.text((64,196+128),"VRAIMENT.",font=F2,fill=(200,100,60))
F3=ImageFont.truetype(SERR,40)
d.text((66,185+112+150),"Un passage. Les poils remontent en boule.",font=F3,fill=(255,255,255))
F4=ImageFont.truetype(SERR,29)
t="Sans recharge ni adhésif  ·  Livraison offerte  ·  Retour 14 jours"
tw=d.textlength(t,font=F4)
d.rectangle([40,1010,W-40,1010+72],fill=(18,18,20))
d.text(((W-tw)/2,1010+20),t,font=F4,fill=(255,255,255))
img.save('/home/user/living-apart-tanger/ads/felins-fideles-meta-4x5.png')
print(px,py,prod.size)
