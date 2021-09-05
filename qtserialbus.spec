#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtserialbus
Version  : 5.15.2
Release  : 25
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtserialbus-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtserialbus-everywhere-src-5.15.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtserialbus-bin = %{version}-%{release}
Requires: qtserialbus-lib = %{version}-%{release}
Requires: qtserialbus-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5SerialPort)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)

%description
No detailed description available

%package bin
Summary: bin components for the qtserialbus package.
Group: Binaries
Requires: qtserialbus-license = %{version}-%{release}

%description bin
bin components for the qtserialbus package.


%package dev
Summary: dev components for the qtserialbus package.
Group: Development
Requires: qtserialbus-lib = %{version}-%{release}
Requires: qtserialbus-bin = %{version}-%{release}
Provides: qtserialbus-devel = %{version}-%{release}
Requires: qtserialbus = %{version}-%{release}

%description dev
dev components for the qtserialbus package.


%package examples
Summary: examples components for the qtserialbus package.
Group: Default
Requires: qtserialbus-dev = %{version}-%{release}

%description examples
examples components for the qtserialbus package.


%package lib
Summary: lib components for the qtserialbus package.
Group: Libraries
Requires: qtserialbus-license = %{version}-%{release}

%description lib
lib components for the qtserialbus package.


%package license
Summary: license components for the qtserialbus package.
Group: Default

%description license
license components for the qtserialbus package.


%prep
%setup -q -n qtserialbus-everywhere-src-5.15.2
cd %{_builddir}/qtserialbus-everywhere-src-5.15.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1630804887
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtserialbus
cp %{_builddir}/qtserialbus-everywhere-src-5.15.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtserialbus/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtserialbus-everywhere-src-5.15.2/LICENSE.GPLv2 %{buildroot}/usr/share/package-licenses/qtserialbus/87d17bf05b5aba91a2091b17a89336fb6a8954e2
cp %{_builddir}/qtserialbus-everywhere-src-5.15.2/LICENSE.GPLv3 %{buildroot}/usr/share/package-licenses/qtserialbus/7d974f34cf5fd474f0fdf6ebc8d410ea5c8b72de
cp %{_builddir}/qtserialbus-everywhere-src-5.15.2/LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtserialbus/d8b489a3c3d500a6601181e3db39bec6124b86fc
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/canbusutil

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qcanbusdevice_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qcanbusdeviceinfo_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbus_symbols_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbusadu_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbusclient_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbuscommevent_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbusdevice_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbusrtuserialmaster_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbusrtuserialslave_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbusserver_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbustcpclient_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qmodbustcpserver_p.h
/usr/include/qt5/QtSerialBus/5.15.2/QtSerialBus/private/qtserialbus-config_p.h
/usr/include/qt5/QtSerialBus/QCanBus
/usr/include/qt5/QtSerialBus/QCanBusDevice
/usr/include/qt5/QtSerialBus/QCanBusDeviceInfo
/usr/include/qt5/QtSerialBus/QCanBusFactory
/usr/include/qt5/QtSerialBus/QCanBusFactoryV2
/usr/include/qt5/QtSerialBus/QCanBusFrame
/usr/include/qt5/QtSerialBus/QModbusClient
/usr/include/qt5/QtSerialBus/QModbusDataUnit
/usr/include/qt5/QtSerialBus/QModbusDataUnitMap
/usr/include/qt5/QtSerialBus/QModbusDevice
/usr/include/qt5/QtSerialBus/QModbusDeviceIdentification
/usr/include/qt5/QtSerialBus/QModbusExceptionResponse
/usr/include/qt5/QtSerialBus/QModbusPdu
/usr/include/qt5/QtSerialBus/QModbusReply
/usr/include/qt5/QtSerialBus/QModbusRequest
/usr/include/qt5/QtSerialBus/QModbusResponse
/usr/include/qt5/QtSerialBus/QModbusRtuSerialMaster
/usr/include/qt5/QtSerialBus/QModbusRtuSerialSlave
/usr/include/qt5/QtSerialBus/QModbusServer
/usr/include/qt5/QtSerialBus/QModbusTcpClient
/usr/include/qt5/QtSerialBus/QModbusTcpConnectionObserver
/usr/include/qt5/QtSerialBus/QModbusTcpServer
/usr/include/qt5/QtSerialBus/QtSerialBus
/usr/include/qt5/QtSerialBus/QtSerialBusDepends
/usr/include/qt5/QtSerialBus/QtSerialBusVersion
/usr/include/qt5/QtSerialBus/qcanbus.h
/usr/include/qt5/QtSerialBus/qcanbusdevice.h
/usr/include/qt5/QtSerialBus/qcanbusdeviceinfo.h
/usr/include/qt5/QtSerialBus/qcanbusfactory.h
/usr/include/qt5/QtSerialBus/qcanbusframe.h
/usr/include/qt5/QtSerialBus/qmodbusclient.h
/usr/include/qt5/QtSerialBus/qmodbusdataunit.h
/usr/include/qt5/QtSerialBus/qmodbusdevice.h
/usr/include/qt5/QtSerialBus/qmodbusdeviceidentification.h
/usr/include/qt5/QtSerialBus/qmodbuspdu.h
/usr/include/qt5/QtSerialBus/qmodbusreply.h
/usr/include/qt5/QtSerialBus/qmodbusrtuserialmaster.h
/usr/include/qt5/QtSerialBus/qmodbusrtuserialslave.h
/usr/include/qt5/QtSerialBus/qmodbusserver.h
/usr/include/qt5/QtSerialBus/qmodbustcpclient.h
/usr/include/qt5/QtSerialBus/qmodbustcpserver.h
/usr/include/qt5/QtSerialBus/qserialbusglobal.h
/usr/include/qt5/QtSerialBus/qtserialbus-config.h
/usr/include/qt5/QtSerialBus/qtserialbusglobal.h
/usr/include/qt5/QtSerialBus/qtserialbusversion.h
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBusConfig.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBusConfigVersion.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBus_PassThruCanBusPlugin.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBus_PeakCanBusPlugin.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBus_SocketCanBusPlugin.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBus_TinyCanBusPlugin.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBus_VirtualCanBusPlugin.cmake
/usr/lib64/libQt5SerialBus.prl
/usr/lib64/libQt5SerialBus.so
/usr/lib64/pkgconfig/Qt5SerialBus.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialbus.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialbus_private.pri

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/serialbus/can/bitratebox.cpp
/usr/share/qt5/examples/serialbus/can/bitratebox.h
/usr/share/qt5/examples/serialbus/can/can.pro
/usr/share/qt5/examples/serialbus/can/can.qrc
/usr/share/qt5/examples/serialbus/can/connectdialog.cpp
/usr/share/qt5/examples/serialbus/can/connectdialog.h
/usr/share/qt5/examples/serialbus/can/connectdialog.ui
/usr/share/qt5/examples/serialbus/can/images/application-exit.png
/usr/share/qt5/examples/serialbus/can/images/clear.png
/usr/share/qt5/examples/serialbus/can/images/connect.png
/usr/share/qt5/examples/serialbus/can/images/disconnect.png
/usr/share/qt5/examples/serialbus/can/main.cpp
/usr/share/qt5/examples/serialbus/can/mainwindow.cpp
/usr/share/qt5/examples/serialbus/can/mainwindow.h
/usr/share/qt5/examples/serialbus/can/mainwindow.ui
/usr/share/qt5/examples/serialbus/can/sendframebox.cpp
/usr/share/qt5/examples/serialbus/can/sendframebox.h
/usr/share/qt5/examples/serialbus/can/sendframebox.ui
/usr/share/qt5/examples/serialbus/modbus/adueditor/adueditor.pro
/usr/share/qt5/examples/serialbus/modbus/adueditor/interface.ui
/usr/share/qt5/examples/serialbus/modbus/adueditor/main.cpp
/usr/share/qt5/examples/serialbus/modbus/adueditor/mainwindow.cpp
/usr/share/qt5/examples/serialbus/modbus/adueditor/mainwindow.h
/usr/share/qt5/examples/serialbus/modbus/adueditor/modbustcpclient.cpp
/usr/share/qt5/examples/serialbus/modbus/adueditor/modbustcpclient.h
/usr/share/qt5/examples/serialbus/modbus/adueditor/modbustcpclient_p.h
/usr/share/qt5/examples/serialbus/modbus/adueditor/plaintextedit.h
/usr/share/qt5/examples/serialbus/modbus/master/images/application-exit.png
/usr/share/qt5/examples/serialbus/modbus/master/images/connect.png
/usr/share/qt5/examples/serialbus/modbus/master/images/disconnect.png
/usr/share/qt5/examples/serialbus/modbus/master/images/settings.png
/usr/share/qt5/examples/serialbus/modbus/master/main.cpp
/usr/share/qt5/examples/serialbus/modbus/master/mainwindow.cpp
/usr/share/qt5/examples/serialbus/modbus/master/mainwindow.h
/usr/share/qt5/examples/serialbus/modbus/master/mainwindow.ui
/usr/share/qt5/examples/serialbus/modbus/master/master.pro
/usr/share/qt5/examples/serialbus/modbus/master/master.qrc
/usr/share/qt5/examples/serialbus/modbus/master/settingsdialog.cpp
/usr/share/qt5/examples/serialbus/modbus/master/settingsdialog.h
/usr/share/qt5/examples/serialbus/modbus/master/settingsdialog.ui
/usr/share/qt5/examples/serialbus/modbus/master/writeregistermodel.cpp
/usr/share/qt5/examples/serialbus/modbus/master/writeregistermodel.h
/usr/share/qt5/examples/serialbus/modbus/modbus.pro
/usr/share/qt5/examples/serialbus/modbus/slave/images/application-exit.png
/usr/share/qt5/examples/serialbus/modbus/slave/images/connect.png
/usr/share/qt5/examples/serialbus/modbus/slave/images/disconnect.png
/usr/share/qt5/examples/serialbus/modbus/slave/images/settings.png
/usr/share/qt5/examples/serialbus/modbus/slave/main.cpp
/usr/share/qt5/examples/serialbus/modbus/slave/mainwindow.cpp
/usr/share/qt5/examples/serialbus/modbus/slave/mainwindow.h
/usr/share/qt5/examples/serialbus/modbus/slave/mainwindow.ui
/usr/share/qt5/examples/serialbus/modbus/slave/settingsdialog.cpp
/usr/share/qt5/examples/serialbus/modbus/slave/settingsdialog.h
/usr/share/qt5/examples/serialbus/modbus/slave/settingsdialog.ui
/usr/share/qt5/examples/serialbus/modbus/slave/slave.pro
/usr/share/qt5/examples/serialbus/modbus/slave/slave.qrc
/usr/share/qt5/examples/serialbus/serialbus.pro

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5SerialBus.so.5
/usr/lib64/libQt5SerialBus.so.5.15
/usr/lib64/libQt5SerialBus.so.5.15.2
/usr/lib64/qt5/plugins/canbus/libqtpassthrucanbus.so
/usr/lib64/qt5/plugins/canbus/libqtpeakcanbus.so
/usr/lib64/qt5/plugins/canbus/libqtsocketcanbus.so
/usr/lib64/qt5/plugins/canbus/libqttinycanbus.so
/usr/lib64/qt5/plugins/canbus/libqtvirtualcanbus.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtserialbus/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtserialbus/7d974f34cf5fd474f0fdf6ebc8d410ea5c8b72de
/usr/share/package-licenses/qtserialbus/87d17bf05b5aba91a2091b17a89336fb6a8954e2
/usr/share/package-licenses/qtserialbus/d8b489a3c3d500a6601181e3db39bec6124b86fc
