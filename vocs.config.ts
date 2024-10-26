import { defineConfig } from "vocs";

export default defineConfig({
  basePath: "/mantrapy",
  title: "Mantra-py",
  sidebar: [
    {
      text: "Getting Started",
      link: "/getting-started",
    },
    {
      text: "Wallet",
      link: "/wallet",
    },
    {
      text: "Webhooks API",
      link: "/webhooks-api",
    },
  ],
});
