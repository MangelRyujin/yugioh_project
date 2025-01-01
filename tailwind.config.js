/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./**/templates/**/*.html","./node_modules/flyonui/dist/js/*.js"],
  darkMode: "media",
  theme: {
    flyonui: {
      themes: ["light", "dark", "gourmet"]
    },
    extend: {},
  },
  plugins: [
    require("flyonui"),
    require("flyonui/plugin"),
    require("tailwindcss-motion"), // Require only if you want to use FlyonUI JS component
  ],
}

