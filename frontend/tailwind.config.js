import frappeUIPreset from "frappe-ui/src/tailwind/preset";
import colors from "tailwindcss/colors";

export default {
	presets: [frappeUIPreset],
	content: [
		"./index.html",
		"./src/**/*.{vue,js,ts,jsx,tsx}",
		"./node_modules/frappe-ui/src/components/**/*.{vue,js,ts,jsx,tsx}",
	],
	theme: {
		extend: {
			colors: {
				primary: "var(--primary-color)",
				secondary: "var(--secondary-color)",
				login: "var(--login-color)",
				sidebar: "var(--sidebar-color)",
				slate: colors.slate,
				emerald: colors.emerald,
			},
		},
	},
	plugins: [],
};
