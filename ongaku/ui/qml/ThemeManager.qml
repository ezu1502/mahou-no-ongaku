pragma Singleton

import QtQuick

// * Exposes the chosen theme's palette to ThemeVision

QtObject {
    property string currentTheme: "Dark"


    readonly property var currentPalette:
        Themes.palettes[currentTheme] ?? Themes.palettes["Dark"]

    function setTheme(theme_name){
        if (Themes.palettes[theme_name] === undefined){
            console.warn("Couldn't find theme:", theme_name);
            return;
        }

        currentTheme = theme_name
    }
}
