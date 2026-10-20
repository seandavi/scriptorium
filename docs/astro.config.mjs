// @ts-check
import { defineConfig } from "astro/config";
import starlight from "@astrojs/starlight";

// GA4 is injected only into production builds. `astro dev` sets
// NODE_ENV=development, so local sessions and CI link-checks don't ship hits.
// Consolidated "Sean Davis — web" property; skipped on non-production hosts.
const gaId = "G-KLLV1GCF4E";
const analyticsHead =
  process.env.NODE_ENV === "production"
    ? [
        {
          tag: "script",
          content:
            `(function(){var h=location.hostname;` +
            `if(h==='localhost'||h==='127.0.0.1'||/\\.(workers\\.dev|netlify\\.app|ts\\.net)$/.test(h)||/^[0-9.]+$/.test(h)||h.indexOf(':')>=0)return;` +
            `var s=document.createElement('script');s.async=true;` +
            `s.src='https://www.googletagmanager.com/gtag/js?id=${gaId}';document.head.appendChild(s);` +
            `window.dataLayer = window.dataLayer || [];` +
            `function gtag(){dataLayer.push(arguments);}window.gtag=gtag;` +
            `gtag('js', new Date());` +
            `gtag('config', '${gaId}', { content_group: 'scriptorium' });})();`,
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
