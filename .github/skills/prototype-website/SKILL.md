---
name: prototype-website
description: "Use when creating a polished single-page prototype website for a hospitality, travel, boutique brand, or landing page. Covers structure, visual design, responsive behavior, accessibility, bilingual support, conversion-focused sections, and lightweight interactions."
---

# Prototype Website Skill

Use this skill to quickly create a high-quality prototype website in a single HTML file with embedded CSS and minimal JavaScript. It is designed for fast concept validation, client presentation, and landing-page-style prototypes that need to feel premium, polished, and mobile-ready.

## Goal

Produce a prototype website that:
- looks premium and modern
- feels credible for a hospitality or lifestyle brand
- works well on desktop and mobile
- includes clear call-to-action moments
- can be opened and reviewed immediately in a browser
- remains easy to edit and extend

## Core Workflow

### 1. Define the brand and the page objective
Before writing code, clarify:
- what the business is
- who the target visitor is
- what the visitor should do next
- which conversion goal is most important (booking, WhatsApp, contact, inquiry, reservation)

Use this to determine the page tone, structure, and CTAs.

### 2. Choose the page structure
Build a clear user flow with these major sections:
- sticky header with brand and navigation
- hero section with strong message and visual treatment
- quick trust/reservation bar near the hero
- brand introduction / welcome section
- key services or property highlights
- proof or lifestyle imagery
- CTA section with direct action buttons
- footer with essential contact info

For hospitality or property brands, prioritize trust signals such as:
- direct booking prompts
- quick booking info
- local context
- service quality indicators
- social proof or descriptive imagery

### 3. Design the visual system
Create a refined, coherent aesthetic using:
- warm, earthy, or premium neutral palettes
- one serif headline style and one clean sans-serif body style
- balanced spacing and generous white space
- subtle borders, shadows, and rounded corners
- consistent button styles and hover states

Recommended design patterns:
- a calming luxury palette with one accent color
- dark overlays on hero imagery for readability
- elevated cards with soft shadows
- high contrast for accessibility
- minimal but intentional motion

### 4. Implement the foundation in HTML
Build a semantic page with:
- doctype and metadata
- viewport setup
- accessible landmarks: header, nav, main, section, footer
- clear heading hierarchy
- buttons and links with strong labels
- descriptive alt text or decorative image handling

Keep the structure simple and maintainable. Prefer semantic sections over complex nested markup.

### 5. Add responsive styling
Write CSS for:
- a centered max-width container
- mobile-first layout defaults
- breakpoint adjustments for tablet and mobile widths
- stacked sections when space is limited
- compact navigation on small screens
- flexible grids for cards and info blocks

Common best practices:
- use `clamp()` for fluid typography
- avoid fixed pixel-heavy layouts
- maintain comfortable line lengths
- ensure buttons remain touch-friendly
- preserve readability for long text and small screens

### 6. Add persuasive interactions
Use lightweight JavaScript only when it meaningfully improves the prototype:
- mobile menu toggle
- hero image rotation or slideshow
- language switch behavior
- reveal-on-scroll animation
- dark/light theme toggle if relevant

Keep interactions subtle and smooth. The site should feel premium, not busy.

### 7. Support multilingual or bilingual presentation when relevant
If the brand serves Arabic and French users or a bilingual audience:
- add language switch buttons in the header
- use appropriate fonts for Arabic text
- support `dir="rtl"` and proper text alignment when needed
- keep copy visually balanced and consistent

For a prototype, the translation can be practical and visually consistent rather than fully translated for every element.

### 8. Add conversion-focused calls to action
Prominent CTA patterns include:
- WhatsApp booking link
- “Book now” button
- “Contact us” button
- “Reserve your stay” form or panel
- direct action with obvious destination and user benefit

Each CTA should be easy to understand and visually prominent.

### 9. Validate the prototype before completion
Check the page for:
- layout consistency
- readability at different widths
- proper button and link clarity
- no broken images or missing assets
- smooth mobile navigation
- accessible contrast and focus states
- working interactions and no console errors

Open the page in a browser and review the full experience end to end.

## Decision Points

### If the page is for a luxury or hospitality brand
Use:
- large cinematic hero image
- editorial typography
- warm neutral palette
- subtle motion
- trust-focused sections and reservation bar

### If the page is for a startup or product landing page
Use:
- more direct headline and feature blocks
- concise sections
- strong benefit-driven text
- conversion sections near the top

### If the page is bilingual
Use:
- Arabic/English or Arabic/French support
- separate font treatment for Arabic text
- switcher UI and mirrored layout adjustments as needed

### If the page needs to be fast and lightweight
Prefer:
- one HTML file
- embedded CSS and JS
- a limited number of images
- no heavy frameworks
- minimal dependencies

## Quality Criteria

The prototype is considered complete when all of the following are true:
- the page has a clear hero and conversion goal
- the design feels intentional and premium
- the layout works across mobile and desktop
- CTAs are visible and persuasive
- visual hierarchy is strong and readable
- accessibility basics are respected
- the page can be opened immediately without setup friction
- the content feels brand-aligned and visually coherent

## Expected Output

A working prototype in a simple structure such as:
- `index.html`
- embedded CSS in a `<style>` block
- optional embedded JavaScript for interactions
- local assets or remote images if needed

## Recommended Execution Pattern

When asked to create a prototype website, do this in order:
1. identify the brand, audience, and conversion goal
2. sketch the required sections
3. choose a premium but practical visual direction
4. build semantic HTML structure
5. apply styles for desktop and mobile responsiveness
6. add only necessary JS interactions
7. check accessibility and usability
8. refine based on the visual quality and clarity
9. produce the final page ready to open in a browser

## Example Prompts

- “Create a premium one-page prototype for a boutique villa brand in Morocco.”
- “Build a modern hospitality landing page with a hero, booking CTA, and bilingual layout.”
- “Make a luxury property website prototype with a sticky nav, warm palette, and WhatsApp booking button.”
- “Create a responsive prototype homepage for a travel brand with strong editorial styling and mobile navigation.”
- “Design a stylish single-page landing page for a guesthouse with Arabic and French support.”

## Related Customizations

Related customizations to create next:
- a reusable prompt for “luxury landing page concept”
- a design-system instruction file for premium prototype styling
- a mobile-first responsive CSS instruction set
- a bilingual website prompt for Arabic/French adaptation
