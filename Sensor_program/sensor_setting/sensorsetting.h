#ifndef SENSORSETTING_H
#define SENSORSETTING_H

#include <QWidget>

namespace Ui {
class SensorSetting;
}

class SensorSetting : public QWidget
{
    Q_OBJECT

public:
    explicit SensorSetting(QWidget *parent = 0);
    ~SensorSetting();

private:
    Ui::SensorSetting *ui;
};

#endif // SENSORSETTING_H
