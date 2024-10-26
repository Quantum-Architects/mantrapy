import { defineConfig } from 'vocs'

export default defineConfig({
  title: 'Docs',
  sidebar: [
    {
      text: 'Getting Started',
      link: '/getting-started',
    },
    {
      text: 'Webhooks API',
      link: '/webhooks-api',
    },
    {
      text: 'Webhooks',
      link: '/webhooks',
    },
  ],
})
