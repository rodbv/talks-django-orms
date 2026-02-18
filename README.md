## Django ORM — performance (talk)

Slides and demo app for a talk on avoiding common Django ORM performance mistakes.

## Slides

- **Live:** [https://rodbv.github.io/talks-django-orms/](https://rodbv.github.io/talks-django-orms/)
- **Local:** `just slides` then open the URL (e.g. http://localhost:3000).
- **GitHub Pages:** On push to `main`, the [Slides workflow](.github/workflows/slides.yml) tests the slides and deploys them. Enable in the repo: **Settings → Pages → Build and deployment → Source:** choose **GitHub Actions**. The site will be at `https://<user>.github.io/<repo>/`.

Slides content lives in [slides/slides.md](slides/slides.md). `node_modules` is not committed; the workflow runs `npm ci` in `slides/` and deploys the resulting directory.
