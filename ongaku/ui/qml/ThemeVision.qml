pragma Singleton
import QtQuick

// * Represents the current theme's palette, updated in real time

QtObject {
    // general
    readonly property color background: ThemeManager.currentPalette.background
    readonly property color foreground: ThemeManager.currentPalette.foreground
    readonly property color mahouHighlight: ThemeManager.currentPalette.mahouHighlight

    // surfaces
    readonly property color surface: ThemeManager.currentPalette.surface
    readonly property color surfaceHover: ThemeManager.currentPalette.surfaceHover
    readonly property color surfacePressed: ThemeManager.currentPalette.surfacePressed

    readonly property color progressBackground: ThemeManager.currentPalette.progressBackground
    readonly property color progress: ThemeManager.currentPalette.progress
    readonly property color preciseMode: ThemeManager.currentPalette.preciseMode
    readonly property color secondaryText: ThemeManager.currentPalette.secondaryText

    // nav
    readonly property color navBackground: ThemeManager.currentPalette.navBackground
    readonly property color navHover: ThemeManager.currentPalette.navHover
    readonly property color navPressed: ThemeManager.currentPalette.navHover
    readonly property color navText: ThemeManager.currentPalette.navText
}