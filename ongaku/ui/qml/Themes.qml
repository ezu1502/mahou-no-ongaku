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

            surface: "#BBBBBB",
            surfaceHover: "#AAAAAA",
            surfacePressed: "#999999",

            progressBackground: "#888888",
            progress: "#472486",
            preciseMode: "#833f4a",
            secondaryText: '#4b4b4b',

            navBackground: "#472486",
            navHover: '#31224d',
            navText: '#e0e0e0'
        },

        "Habanero": {
            background: '#17181d',
            foreground: "#DDDDDD",
            mahouHighlight: "#ef3200",

            surface: '#242427',
            surfaceHover: '#313135',
            surfacePressed: '#3b3b42',

            progressBackground: "#292726",
            progress: "#ef3200",
            preciseMode: '#1b4657',
            secondaryText: "#888888",

            navBackground: "#ef3200",
            navHover: '#e45832',
            navPressed: '#cdb4fa',
            navText: '#17181d'
        },

        "Monochrome": {
            background: '#484966',
            foreground: "#EEEEEE",
            mahouHighlight: '#9095e9',

            surface: '#383952',
            surfaceHover: '#2f3047',
            surfacePressed: '#232436',

            progressBackground: "#2f3047",
            progress: "#9095e9",
            preciseMode: '#1116aa',
            secondaryText: '#AAAAAA',

            navBackground: '#9095e9',
            navHover: '#6f75e7',
            navPressed: '#7175c5',
            navText: '#2f3047'
        },
        
        "Cheesecake": {
            background: "#E8D1B7",
            foreground: '#3a2f26',
            mahouHighlight: '#900005',

            surface: '#b4978b',
            surfaceHover: '#9c8276',
            surfacePressed: '#9b8074',

            progressBackground: "#a5897d",
            progress: "#900005",
            preciseMode: '#d81445',
            secondaryText: '#36312b',

            navBackground: "#900005",
            navHover: '#963a49',
            navText: '#e7dacb'
        },

        "Future": {
            background: '#101d24',
            foreground: '#a0f1fd',
            mahouHighlight: '#203946',

            surface: '#2a3135',
            surfaceHover: '#424b50',
            surfacePressed: '#5f6366',

            progressBackground: "#424b50",
            progress: '#57f4ff',
            preciseMode: "#833f4a",
            secondaryText: "#888888",

            navBackground: "#203946",
            navHover: '#284e63',
            navPressed: '#23536d',
            navText: '#a0f1fd'
        },


    })
}