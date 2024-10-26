import { defineConfig } from "vocs";

export default defineConfig({
    basePath: "/mantrapy",
    iconUrl: {
        light: "/icon-snake-gradient.svg",
        dark: "/icon-snake-white.svg",
    },
    logoUrl: {
        light: "/logo-snake-black.svg",
        dark: "/logo-snake-gradient.svg",
    },
    font: {
        google: 'FT Sterling',
    },
    title: "mantra-py",
    socials: [
        {
            icon: 'github',
            link: 'https://github.com/Quantum-Architects',
        },
    ],
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
