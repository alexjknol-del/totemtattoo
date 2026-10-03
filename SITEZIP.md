# totemtattoo.nl

site.zip is de volledige site. Cloudflare Pages (account Patricia, project totemtattoo-git) pakt die bij elke push op main uit:

- Build command: `python3 -m zipfile -e site.zip dist`
- Build output directory: `dist`

Bijwerken: nieuwe site.zip uploaden en committen.
