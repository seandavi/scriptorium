// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// GA4 is injected only into production builds. `astro dev` sets
// NODE_ENV=development, so local sessions and CI link-checks don't ship hits.
// Override the ID with GA_MEASUREMENT_ID to point at a different property.
const gaId = process.env.GA_MEASUREMENT_ID ?? "G-SWLJ3Z90W9";
const analyticsHead =
  process.env.NODE_ENV === "production"
    ? [
        {
          tag: "script",
          attrs: { async: true, src: `https://www.googletagmanager.com/gtag/js?id=${gaId}` },
        },
        {
          tag: "script",
          content:
            `window.dataLayer = window.dataLayer || [];` +
            `function gtag(){dataLayer.push(arguments);}` +
            `gtag('js', new Date());` +
            `gtag('config', '${gaId}');`,
        },
      ]
    : [];

export default defineConfig({
  // GitHub Pages target. Override BASE/SITE in CI when deploying elsewhere.
  site: process.env.SITE ?? "https://seandavi.github.io",
  base: process.env.BASE ?? "/scriptorium",
  integrations: [
    starlight({
      title: "Scriptorium",
      head: analyticsHead,
      description:
        "AI-assisted skills for scholarly writing — citation audit, simulated peer review, argumentative-flow analysis — sharing one editorial state file and grounded in a peer-reviewed evidence base.",
      logo: {
        src: "./src/assets/scriptorium-mark.png",
        alt: "Scriptorium",
        replacesTitle: false,
      },
      customCss: ["./src/styles/landing.css"],
      social: [
        {
          icon: "github",
          label: "GitHub",
          href: "https://github.com/seandavi/scriptorium",
        },
      ],
      // Diátaxis-style sidebar (three quadrants). Tutorials was dropped —
      // the user-facing docs are shaped how-to-first, with Concepts
      // carrying the project's evidence-base mass. Concepts is the
      // largest section — the knowledge layer renders under it as
      // auto-generated subsections from the preprocess step.
      sidebar: [
        { label: "Roadmap", link: "/roadmap/" },
        {
          label: "How-to guides",
          items: [{ autogenerate: { directory: "how-to" } }],
        },
        {
          label: "Reference",
          items: [{ autogenerate: { directory: "reference" } }],
        },
        {
          label: "Concepts",
          collapsed: false,
          items: [{ autogenerate: { directory: "concepts" } }],
        },
      ],
      editLink: {
        baseUrl:
          "https://github.com/seandavi/scriptorium/edit/main/docs/",
      },
      lastUpdated: true,
      pagination: true,
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 3 },
    }),
  ],
});
