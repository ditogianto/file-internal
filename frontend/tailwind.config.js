/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        tactical: {
          dark: '#080c13',
          card: '#0d131f',
          surface: '#141d2e',
          border: '#1e293b',
          brand: '#059669',
          brandDark: '#064e3b',
          safe: '#10b981',
          warning: '#f59e0b',
          danger: '#ef4444',
          accent: '#06b6d4'
        }
      },
      fontFamily: {
        mono: ['"JetBrains Mono"', 'Consolas', 'Monaco', 'monospace']
      }
    },
  },
  plugins: [],
}
