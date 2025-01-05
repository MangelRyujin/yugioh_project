/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./**/templates/**/*.html","./node_modules/flyonui/dist/js/*.js"],
  plugins: [
    require("flyonui"),
    require("flyonui/plugin"),
    require("tailwindcss-motion"), // Require only if you want to use FlyonUI JS component
  ],
  theme: {
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
  flyonui: {
    themes: ['light', 'dark']
  },
  darkMode: ['class', '[data-theme="dark"]'],
  
  
}

