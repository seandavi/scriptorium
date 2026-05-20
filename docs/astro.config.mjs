// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

export default defineConfig({
  // GitHub Pages target. Override BASE/SITE in CI when deploying elsewhere.
  site: process.env.SITE ?? "https://seandavi.github.io",
  base: process.env.BASE ?? "/scriptorium",
  integrations: [
    starlight({
      title: "Scriptorium",
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
