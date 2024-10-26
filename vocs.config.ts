import { defineConfig } from "vocs";

export default defineConfig({
  basePath: "/mantrapy",
  iconUrl: {
    light: "/Icon-gradient.svg",
    dark: "/Icon-white.svg",
  },
  logoUrl: {
    light: "/logo-black.svg",
    dark: "/logo-gradient.svg",
  },
  font: {
    google: 'FT Sterling',
  },
  title: "mantra-py",
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
          link: "/examples/webhooks-api",
        },
      ],
    },
  ],
});
