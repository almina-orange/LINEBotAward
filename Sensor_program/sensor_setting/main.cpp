#include "sensorsetting.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    SensorSetting w;
    w.show();

    return a.exec();
}
