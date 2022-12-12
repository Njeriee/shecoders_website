/** @type {import('tailwindcss').Config} */
module.exports = {
  content:["./src/**/*.{html,js}","./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      backgroundImage:{
        'hero-bg':"url('/src/images/herobg.jpg')"
      }
    },
  },
  plugins: [
    require('flowbite/plugin')
  ],
}
