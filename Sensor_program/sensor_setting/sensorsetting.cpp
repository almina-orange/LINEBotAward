#include "sensorsetting.h"
#include "ui_sensorsetting.h"

SensorSetting::SensorSetting(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SensorSetting)
{
    ui->setupUi(this);
}

SensorSetting::~SensorSetting()
{
    delete ui;
}
