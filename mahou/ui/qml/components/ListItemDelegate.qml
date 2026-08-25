import QtQuick
import QtQuick.Controls.Basic

Rectangle {
    id: itemDelegate
    height: 45

    property ListView listView
    property int itemIndex

    property bool selected: ListView.isCurrentItem

    property color bgColor: selected ? "#343434" : itemMouseArea.hovered ? "#2C2C2C" : "#181818"
    property color bgHighlightColor: selected ? "#3A3A3A" : itemMouseArea.hovered ? "#303030" : "#202020"


    MouseArea {
        id: itemMouseArea
        anchors.fill: parent

        hoverEnabled: true

        property bool hovered: false

        onEntered: {
            hovered = true
        }
        onExited: {
            hovered = false
        }

        onClicked: {
            itemDelegate.listView.currentIndex = itemDelegate.itemIndex
        }
    }

    gradient: Gradient {

        orientation: Gradient.Horizontal

        GradientStop {
            position: 0.0
            color: itemDelegate.bgColor
        }
        
        GradientStop {
            position: 1.0
            color: itemDelegate.itemIndex % 2 === 0 ? itemDelegate.bgHighlightColor : itemDelegate.bgColor
        }

    }

    Behavior on bgColor {
        ColorAnimation {
            duration: 80
        }
    }

    Behavior on bgHighlightColor {
        ColorAnimation {
            duration: 80
        }
    }
    
    Column {
        anchors.left: parent.left
        anchors.verticalCenter: parent.verticalCenter

        anchors.leftMargin: 10

        Text {
            text: model.title

            color: "#EEEEEE"

            font.family: "M PLUS 1p"
            font.pixelSize: 16

            font.weight: 500
        }
        Text {
            text: model.artist

            color: '#868585'

            font.family: "M PLUS 1p"
            font.pixelSize: 12

            font.weight: 500
        }

    }

}