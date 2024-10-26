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
      text: "Modules",
      items: [
        {
          text: "Wallet",
          link: "/wallet",
        },
        {
          text: "Client",
          link: "/client",
        },
        {
          text: "TxBuilder",
          link: "/txbuilder",
        },
        {
          text: "Webhooks",
          link: "/webhooks",
        },
        {
          text: "Constants",
          link: "/constants",
        },
      ],
    },
    {
      text: "Examples",
      items: [
        {
          text: "Webhooks API",
          link: "/webhooks-api",
        },
      ],
    },
  ],
});
