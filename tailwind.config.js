/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./**/templates/**/*.html","./node_modules/flyonui/dist/js/*.js"],
  darkMode: "media",
  theme: {
    flyonui: {
      themes: ["light", "dark", "gourmet"]
    },
    extend: {
      fontFamily: {

      },
      'animation': {
            'text':'text 5s ease infinite',
        },
        'keyframes': {
            'text': {
                '0%, 100%': {
                   'background-size':'200% 200%',
                    'background-position': 'left center'
                },
                '50%': {
                   'background-size':'200% 200%',
                    'background-position': 'right center'
                }
            },
        }
    },
  },
  plugins: [
    require("flyonui"),
    require("flyonui/plugin"),
    require("tailwindcss-motion"), // Require only if you want to use FlyonUI JS component
  ],
  
}

