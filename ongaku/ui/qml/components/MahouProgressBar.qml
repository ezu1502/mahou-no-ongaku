pragma ComponentBehavior: Bound

import QtQuick
import QtQuick.Controls.Basic
import ".."

import "../js/utilities.js" as Utilities


Item {
    id: root
    width: 300
    height: 10

    property color bg: ThemeVision.progressBackground
    property color progressColor: ThemeVision.progress
    property color preciseModeColor: ThemeVision.preciseMode

    property real progressPercent: 0
    property bool preciseMode: false

    property int durationSeconds: 0 

    

    Rectangle {
        id: track
        color: root.bg
        anchors.fill: parent
        radius: root.height / 2

        Rectangle {
            id: progress

            color: root.preciseMode ? root.preciseModeColor : root.progressColor

            anchors.left: parent.left

            width: root.progressPercent * track.width
            height: track.height

            radius: track.radius

            Behavior on color {
                ColorAnimation {
                    duration: 100
                }
            }
        }        
    }
    
    Row {
        anchors.top: track.bottom
        anchors.right: root.right

        MahouTitle {
            id: progressLabel

            text: Utilities.format_time(root.progressPercent * root.durationSeconds) + " / "

            font.pixelSize: 16
        }

        MahouTitle {
            id: durationLabel

            text: Utilities.format_time(root.durationSeconds)

            font.pixelSize: 16

            color: ThemeVision.secondaryText
        }

    }
    
    MouseArea {
        id: mouseArea
        anchors.fill: track

        property real lastMouseX: 0
        property real mouseStartY: 0


        onPressed: (mouse) => {
            lastMouseX = mouse.x
            mouseStartY = mouse.y
        }

        

        onPositionChanged: (mouse) => {
            if (!pressed){
                return;
            }
                
            let deltaX = mouse.x - lastMouseX;

            let deltaY = Math.abs(mouse.y - mouseStartY);

            let weight = 1;

            if (deltaY > 150){
                weight = 0.4;
                root.preciseMode = true;
            }
            else {
                weight = 1;
                root.preciseMode = false;
            }

            let absoluteProgress = root.progressPercent * track.width;
            root.progressPercent = Utilities.clamp(((absoluteProgress + deltaX * weight) / track.width), 0, 1);

            lastMouseX = mouse.x
        }

        onReleased: {
            root.preciseMode = false;

            backend.set_player_position(root.progressPercent * root.durationSeconds * 1000);
        }
    }

    Connections {
        target: backend

        function onPositionChanged(position){
            if (mouseArea.pressed){
                return;
            }
                
            if (root.durationSeconds > 0){
                root.progressPercent = ((position / 1000) / root.durationSeconds);
            }
            else {
                root.progressPercent = 0;
            }
        }

        function onDurationChanged(duration){
            root.durationSeconds = (duration / 1000);
        }
    }

    

}