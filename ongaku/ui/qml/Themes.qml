pragma Singleton

import QtQuick

// * Contains Mahou's palettes for each theme

QtObject {
    readonly property var palettes: ({
        "Dark": {
            background: "#111111",
            foreground: "#EEEEEE",
            mahouHighlight: "#6f33df",

            surface: "#222222",
            surfaceHover: "#333333",
            surfacePressed: "#444444",

            progressBackground: "#303030",
            progress: "#8744a1",
            preciseMode: "#833f4a",
            secondaryText: "#888888",

            navBackground: "#6f33df",
            navHover: '#8659da',
            navPressed: '#9d85ca',
            navText: "#111111"
        },

        "Light": {
            background: "#CFCFCF",
            foreground: "#222222",
            mahouHighlight: '#472486',

            surface: "#999999",
            surfaceHover: "#888888",
            surfacePressed: "#777777",

            progressBackground: "#888888",
            progress: "#472486",
            preciseMode: "#833f4a",
            secondaryText: '#4b4b4b',

            navBackground: "#472486",
            navHover: '#31224d',
            navText: '#e0e0e0'
        },

        "Habanero": {

        },

        "Monochrome": {

        }
    })
}