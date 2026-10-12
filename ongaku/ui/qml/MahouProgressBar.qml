pragma ComponentBehavior: Bound

import QtQuick
import QtQuick.Controls.Basic

Item {
    id: root
    width: 300
    height: 10

    property color bg: "#303030"
    property color progressColor: "#8744a1"
    property color preciseModeColor: '#833f4a'

    property real progressPercent: 0
    property bool preciseMode: false

    property int durationSeconds: 0 
    property int playerProgress: 0



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

            text: "0:00 / "

            font.pixelSize: 16
        }

        MahouTitle {
            id: durationLabel

            text: "0:00"

            font.pixelSize: 16

            color: "#888888"
        }

    }
    
    MouseArea {
        anchors.fill: track

        property real lastMouseX: 0
        property real mouseStartY: 0


        onPressed: (mouse) => {
            lastMouseX = mouse.x
            mouseStartY = mouse.y
        }

        function clamp(variable, minimum, maximum){
            return Math.max(minimum, Math.min(maximum, variable));
        }

        onPositionChanged: (mouse) => {
            if (!pressed){
                return;
            }
                
            let deltaX = mouse.x - lastMouseX;

            let deltaY = Math.abs(mouse.y - mouseStartY);

            let weight = 1;


            let absoluteProgress = root.progressPercent * track.width;

            if (deltaY > 150){
                weight = 0.4;
                root.preciseMode = true;
            }
            else {
                weight = 1;
                root.preciseMode = false;
            }

            root.progressPercent = clamp(((absoluteProgress + deltaX * weight) / track.width), 0, 1);

            lastMouseX = mouse.x
        }

        onDoubleClicked: (mouse) => {
            root.progressPercent = clamp((mouse.x) / track.width, 0, 1);
        }

        onReleased: {
            root.preciseMode = false;
        }
    }

    

}