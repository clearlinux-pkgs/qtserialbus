#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtserialbus
Version  : 5.10.1
Release  : 4
URL      : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtserialbus-everywhere-src-5.10.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtserialbus-everywhere-src-5.10.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-2.0 GPL-3.0 LGPL-3.0
Requires: qtserialbus-bin
Requires: qtserialbus-lib
BuildRequires : cmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5SerialPort)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qtbase-dev

%description
No detailed description available

%package bin
Summary: bin components for the qtserialbus package.
Group: Binaries

%description bin
bin components for the qtserialbus package.


%package dev
Summary: dev components for the qtserialbus package.
Group: Development
Requires: qtserialbus-lib
Requires: qtserialbus-bin
Provides: qtserialbus-devel

%description dev
dev components for the qtserialbus package.


%package lib
Summary: lib components for the qtserialbus package.
Group: Libraries

%description lib
lib components for the qtserialbus package.


%prep
%setup -q -n qtserialbus-everywhere-src-5.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
qmake QMAKE_CFLAGS="$CFLAGS" QMAKE_CXXFLAGS="$CXXFLAGS" QMAKE_LFLAGS="$LDFLAGS" \
    QMAKE_CFLAGS_RELEASE= QMAKE_CXXFLAGS_RELEASE=
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/canbusutil

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qcanbusdevice_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qcanbusdeviceinfo_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbus_symbols_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbusadu_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbusclient_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbuscommevent_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbusdevice_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbusrtuserialmaster_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbusrtuserialslave_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbusserver_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbustcpclient_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qmodbustcpserver_p.h
/usr/include/qt5/QtSerialBus/5.10.1/QtSerialBus/private/qtserialbus-config_p.h
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
/usr/include/qt5/QtSerialBus/qtserialbusversion.h
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBusConfig.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBusConfigVersion.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBus_PeakCanBusPlugin.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBus_SocketCanBusPlugin.cmake
/usr/lib64/cmake/Qt5SerialBus/Qt5SerialBus_TinyCanBusPlugin.cmake
/usr/lib64/libQt5SerialBus.la
/usr/lib64/libQt5SerialBus.prl
/usr/lib64/libQt5SerialBus.so
/usr/lib64/pkgconfig/Qt5SerialBus.pc
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialbus.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_serialbus_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5SerialBus.so.5
/usr/lib64/libQt5SerialBus.so.5.10
/usr/lib64/libQt5SerialBus.so.5.10.1
/usr/lib64/qt5/plugins/canbus/libqtpeakcanbus.so
/usr/lib64/qt5/plugins/canbus/libqtsocketcanbus.so
/usr/lib64/qt5/plugins/canbus/libqttinycanbus.so
