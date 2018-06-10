/********************************************************************************
** Form generated from reading UI file 'sensorsetting.ui'
**
** Created by: Qt User Interface Compiler version 5.7.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SENSORSETTING_H
#define UI_SENSORSETTING_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSlider>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_SensorSetting
{
public:
    QTabWidget *tabWidget;
    QWidget *tab;
    QWidget *verticalLayoutWidget;
    QVBoxLayout *verticalLayout;
    QHBoxLayout *horizontalLayout;
    QCheckBox *checkBox;
    QSlider *horizontalSlider;
    QHBoxLayout *horizontalLayout_4;
    QCheckBox *checkBox_2;
    QSlider *horizontalSlider_2;
    QHBoxLayout *horizontalLayout_3;
    QCheckBox *checkBox_3;
    QSlider *horizontalSlider_3;
    QHBoxLayout *horizontalLayout_18;
    QHBoxLayout *horizontalLayout_20;
    QLabel *label;
    QLineEdit *lineEdit;
    QHBoxLayout *horizontalLayout_21;
    QLabel *label_2;
    QLineEdit *lineEdit_2;
    QHBoxLayout *horizontalLayout_23;
    QLabel *label_4;
    QLineEdit *lineEdit_4;
    QWidget *tab_2;
    QWidget *verticalLayoutWidget_2;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout_5;
    QCheckBox *checkBox_4;
    QSlider *horizontalSlider_4;
    QHBoxLayout *horizontalLayout_7;
    QCheckBox *checkBox_5;
    QSlider *horizontalSlider_5;
    QHBoxLayout *horizontalLayout_6;
    QCheckBox *checkBox_6;
    QSlider *horizontalSlider_6;
    QHBoxLayout *horizontalLayout_19;
    QHBoxLayout *horizontalLayout_24;
    QLabel *label_5;
    QLineEdit *lineEdit_5;
    QHBoxLayout *horizontalLayout_25;
    QLabel *label_6;
    QLineEdit *lineEdit_6;
    QHBoxLayout *horizontalLayout_26;
    QLabel *label_7;
    QLineEdit *lineEdit_7;
    QPushButton *pushButton;

    void setupUi(QWidget *SensorSetting)
    {
        if (SensorSetting->objectName().isEmpty())
            SensorSetting->setObjectName(QStringLiteral("SensorSetting"));
        SensorSetting->resize(600, 400);
        tabWidget = new QTabWidget(SensorSetting);
        tabWidget->setObjectName(QStringLiteral("tabWidget"));
        tabWidget->setGeometry(QRect(10, 10, 570, 320));
        tab = new QWidget();
        tab->setObjectName(QStringLiteral("tab"));
        verticalLayoutWidget = new QWidget(tab);
        verticalLayoutWidget->setObjectName(QStringLiteral("verticalLayoutWidget"));
        verticalLayoutWidget->setGeometry(QRect(19, 19, 521, 251));
        verticalLayout = new QVBoxLayout(verticalLayoutWidget);
        verticalLayout->setSpacing(6);
        verticalLayout->setContentsMargins(11, 11, 11, 11);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        checkBox = new QCheckBox(verticalLayoutWidget);
        checkBox->setObjectName(QStringLiteral("checkBox"));

        horizontalLayout->addWidget(checkBox);

        horizontalSlider = new QSlider(verticalLayoutWidget);
        horizontalSlider->setObjectName(QStringLiteral("horizontalSlider"));
        horizontalSlider->setOrientation(Qt::Horizontal);

        horizontalLayout->addWidget(horizontalSlider);


        verticalLayout->addLayout(horizontalLayout);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        checkBox_2 = new QCheckBox(verticalLayoutWidget);
        checkBox_2->setObjectName(QStringLiteral("checkBox_2"));

        horizontalLayout_4->addWidget(checkBox_2);

        horizontalSlider_2 = new QSlider(verticalLayoutWidget);
        horizontalSlider_2->setObjectName(QStringLiteral("horizontalSlider_2"));
        horizontalSlider_2->setOrientation(Qt::Horizontal);

        horizontalLayout_4->addWidget(horizontalSlider_2);


        verticalLayout->addLayout(horizontalLayout_4);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        checkBox_3 = new QCheckBox(verticalLayoutWidget);
        checkBox_3->setObjectName(QStringLiteral("checkBox_3"));

        horizontalLayout_3->addWidget(checkBox_3);

        horizontalSlider_3 = new QSlider(verticalLayoutWidget);
        horizontalSlider_3->setObjectName(QStringLiteral("horizontalSlider_3"));
        horizontalSlider_3->setOrientation(Qt::Horizontal);

        horizontalLayout_3->addWidget(horizontalSlider_3);


        verticalLayout->addLayout(horizontalLayout_3);

        horizontalLayout_18 = new QHBoxLayout();
        horizontalLayout_18->setSpacing(20);
        horizontalLayout_18->setObjectName(QStringLiteral("horizontalLayout_18"));
        horizontalLayout_20 = new QHBoxLayout();
        horizontalLayout_20->setSpacing(6);
        horizontalLayout_20->setObjectName(QStringLiteral("horizontalLayout_20"));
        label = new QLabel(verticalLayoutWidget);
        label->setObjectName(QStringLiteral("label"));

        horizontalLayout_20->addWidget(label);

        lineEdit = new QLineEdit(verticalLayoutWidget);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));

        horizontalLayout_20->addWidget(lineEdit);


        horizontalLayout_18->addLayout(horizontalLayout_20);

        horizontalLayout_21 = new QHBoxLayout();
        horizontalLayout_21->setSpacing(6);
        horizontalLayout_21->setObjectName(QStringLiteral("horizontalLayout_21"));
        label_2 = new QLabel(verticalLayoutWidget);
        label_2->setObjectName(QStringLiteral("label_2"));

        horizontalLayout_21->addWidget(label_2);

        lineEdit_2 = new QLineEdit(verticalLayoutWidget);
        lineEdit_2->setObjectName(QStringLiteral("lineEdit_2"));

        horizontalLayout_21->addWidget(lineEdit_2);


        horizontalLayout_18->addLayout(horizontalLayout_21);

        horizontalLayout_23 = new QHBoxLayout();
        horizontalLayout_23->setSpacing(6);
        horizontalLayout_23->setObjectName(QStringLiteral("horizontalLayout_23"));
        label_4 = new QLabel(verticalLayoutWidget);
        label_4->setObjectName(QStringLiteral("label_4"));

        horizontalLayout_23->addWidget(label_4);

        lineEdit_4 = new QLineEdit(verticalLayoutWidget);
        lineEdit_4->setObjectName(QStringLiteral("lineEdit_4"));

        horizontalLayout_23->addWidget(lineEdit_4);


        horizontalLayout_18->addLayout(horizontalLayout_23);


        verticalLayout->addLayout(horizontalLayout_18);

        tabWidget->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QStringLiteral("tab_2"));
        verticalLayoutWidget_2 = new QWidget(tab_2);
        verticalLayoutWidget_2->setObjectName(QStringLiteral("verticalLayoutWidget_2"));
        verticalLayoutWidget_2->setGeometry(QRect(19, 19, 521, 251));
        verticalLayout_2 = new QVBoxLayout(verticalLayoutWidget_2);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        horizontalLayout_5 = new QHBoxLayout();
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        checkBox_4 = new QCheckBox(verticalLayoutWidget_2);
        checkBox_4->setObjectName(QStringLiteral("checkBox_4"));

        horizontalLayout_5->addWidget(checkBox_4);

        horizontalSlider_4 = new QSlider(verticalLayoutWidget_2);
        horizontalSlider_4->setObjectName(QStringLiteral("horizontalSlider_4"));
        horizontalSlider_4->setEnabled(true);
        horizontalSlider_4->setOrientation(Qt::Horizontal);

        horizontalLayout_5->addWidget(horizontalSlider_4);


        verticalLayout_2->addLayout(horizontalLayout_5);

        horizontalLayout_7 = new QHBoxLayout();
        horizontalLayout_7->setSpacing(6);
        horizontalLayout_7->setObjectName(QStringLiteral("horizontalLayout_7"));
        checkBox_5 = new QCheckBox(verticalLayoutWidget_2);
        checkBox_5->setObjectName(QStringLiteral("checkBox_5"));

        horizontalLayout_7->addWidget(checkBox_5);

        horizontalSlider_5 = new QSlider(verticalLayoutWidget_2);
        horizontalSlider_5->setObjectName(QStringLiteral("horizontalSlider_5"));
        horizontalSlider_5->setOrientation(Qt::Horizontal);

        horizontalLayout_7->addWidget(horizontalSlider_5);


        verticalLayout_2->addLayout(horizontalLayout_7);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        checkBox_6 = new QCheckBox(verticalLayoutWidget_2);
        checkBox_6->setObjectName(QStringLiteral("checkBox_6"));

        horizontalLayout_6->addWidget(checkBox_6);

        horizontalSlider_6 = new QSlider(verticalLayoutWidget_2);
        horizontalSlider_6->setObjectName(QStringLiteral("horizontalSlider_6"));
        horizontalSlider_6->setOrientation(Qt::Horizontal);

        horizontalLayout_6->addWidget(horizontalSlider_6);


        verticalLayout_2->addLayout(horizontalLayout_6);

        horizontalLayout_19 = new QHBoxLayout();
        horizontalLayout_19->setSpacing(6);
        horizontalLayout_19->setObjectName(QStringLiteral("horizontalLayout_19"));
        horizontalLayout_24 = new QHBoxLayout();
        horizontalLayout_24->setSpacing(6);
        horizontalLayout_24->setObjectName(QStringLiteral("horizontalLayout_24"));
        label_5 = new QLabel(verticalLayoutWidget_2);
        label_5->setObjectName(QStringLiteral("label_5"));

        horizontalLayout_24->addWidget(label_5);

        lineEdit_5 = new QLineEdit(verticalLayoutWidget_2);
        lineEdit_5->setObjectName(QStringLiteral("lineEdit_5"));

        horizontalLayout_24->addWidget(lineEdit_5);


        horizontalLayout_19->addLayout(horizontalLayout_24);

        horizontalLayout_25 = new QHBoxLayout();
        horizontalLayout_25->setSpacing(6);
        horizontalLayout_25->setObjectName(QStringLiteral("horizontalLayout_25"));
        label_6 = new QLabel(verticalLayoutWidget_2);
        label_6->setObjectName(QStringLiteral("label_6"));

        horizontalLayout_25->addWidget(label_6);

        lineEdit_6 = new QLineEdit(verticalLayoutWidget_2);
        lineEdit_6->setObjectName(QStringLiteral("lineEdit_6"));

        horizontalLayout_25->addWidget(lineEdit_6);


        horizontalLayout_19->addLayout(horizontalLayout_25);

        horizontalLayout_26 = new QHBoxLayout();
        horizontalLayout_26->setSpacing(6);
        horizontalLayout_26->setObjectName(QStringLiteral("horizontalLayout_26"));
        label_7 = new QLabel(verticalLayoutWidget_2);
        label_7->setObjectName(QStringLiteral("label_7"));

        horizontalLayout_26->addWidget(label_7);

        lineEdit_7 = new QLineEdit(verticalLayoutWidget_2);
        lineEdit_7->setObjectName(QStringLiteral("lineEdit_7"));

        horizontalLayout_26->addWidget(lineEdit_7);


        horizontalLayout_19->addLayout(horizontalLayout_26);


        verticalLayout_2->addLayout(horizontalLayout_19);

        tabWidget->addTab(tab_2, QString());
        pushButton = new QPushButton(SensorSetting);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setGeometry(QRect(480, 350, 90, 30));

        retranslateUi(SensorSetting);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(SensorSetting);
    } // setupUi

    void retranslateUi(QWidget *SensorSetting)
    {
        SensorSetting->setWindowTitle(QApplication::translate("SensorSetting", "SensorSetting", Q_NULLPTR));
        checkBox->setText(QApplication::translate("SensorSetting", "x", Q_NULLPTR));
        checkBox_2->setText(QApplication::translate("SensorSetting", "y", Q_NULLPTR));
        checkBox_3->setText(QApplication::translate("SensorSetting", "z", Q_NULLPTR));
        label->setText(QApplication::translate("SensorSetting", "x", Q_NULLPTR));
        label_2->setText(QApplication::translate("SensorSetting", "y", Q_NULLPTR));
        label_4->setText(QApplication::translate("SensorSetting", "z", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("SensorSetting", "Tab 1", Q_NULLPTR));
        checkBox_4->setText(QApplication::translate("SensorSetting", "x", Q_NULLPTR));
        checkBox_5->setText(QApplication::translate("SensorSetting", "y", Q_NULLPTR));
        checkBox_6->setText(QApplication::translate("SensorSetting", "z", Q_NULLPTR));
        label_5->setText(QApplication::translate("SensorSetting", "x", Q_NULLPTR));
        label_6->setText(QApplication::translate("SensorSetting", "y", Q_NULLPTR));
        label_7->setText(QApplication::translate("SensorSetting", "z", Q_NULLPTR));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("SensorSetting", "Tab 2", Q_NULLPTR));
        pushButton->setText(QApplication::translate("SensorSetting", "OK", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class SensorSetting: public Ui_SensorSetting {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SENSORSETTING_H
