# ContractorRules design system

Direction: **"Site plan"**. A charcoal drawing board with a faint blueprint grid, an amber measuring tape along the edge,
and the builder's square from the logo. Plain, sturdy, quick to scan on a phone in a truck.
Same speed rules as VisaTide: no web fonts, CSS inlined in every page, tiny JS.

Not based on a survey of comparable sites (no reference library was connected); it follows the existing logo and the rules below.

## Color

| Token | Value | Role |
| --- | --- | --- |
| `--char` | #1F2A33 | Header, hero, primary buttons, headings |
| `--char-2` | #2C3A45 | Hover on charcoal, raised dark surfaces |
| `--amber` | #F2A71B | Brand accent: tape, focus ring, active nav, one key figure |
| `--amber-ink` | #8A5A00 | Amber text and links on light (5.6:1 on white) |
| `--paper` | #F3F1EC | Page background (warm drafting paper) |
| `--card` | #FFFFFF | Cards, tables, inputs |
| `--sand` | #FBF3E2 | Amber-tinted fills: notices, tags |
| `--ink` | #1F2A33 | Body text |
| `--ink-2` | #55626D | Secondary text |
| `--line` | #DDD8CE | Borders and rules |
| `--fog` | #C9CFD4 | Secondary text on charcoal |
| `--ok` / `--bad` | #2F7A4B / #A23A22 | Size-check results |

## Typography

System stack (Roboto on Android, San Francisco on iPhone), tabular figures.
Display clamp(32px, 6vw, 54px)/1.05 at 800; H2 clamp(22px, 3vw, 28px) at 750; H3 19px at 700; body 17px/1.6; small 15px; micro 13px.

## Spacing, shape, depth

8-based spacing; sections 56px desktop, 32px phone; width 1100px. Radius 6 (inputs, tags) and 10 (cards, tables). One shadow on the hero panel only; everything else uses 1px `--line` borders.

## Components

- **Header**: charcoal with a 4px amber bottom rule; inline logo (amber square, white check); scrollable nav row on phones.
- **Hero**: charcoal with a faint blueprint grid (CSS gradients, no image) and an amber tape strip with tick marks along the bottom edge.
- **Stat strip** of key numbers in the hero; one value carries the amber marker.
- **Lookup panel**: white card overlapping the hero edge, holding the NAICS lookup.
- **Cards, tables, buttons, inputs**: as VisaTide, recoloured; focus ring 3px amber.

## Imagery

No photos or icon fonts. The square-and-check logo and the tape strip are the only graphics.
