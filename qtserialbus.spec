#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtserialbus
Version  : 5.12.0
Release  : 14
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtserialbus-everywhere-src-5.12.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtserialbus-everywhere-src-5.12.0.tar.xz
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

%description dev
dev components for the qtserialbus package.


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
%setup -q -n qtserialbus-everywhere-src-5.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1544047863
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtserialbus
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtserialbus/LICENSE.FDL
cp LICENSE.GPLv2 %{buildroot}/usr/share/package-licenses/qtserialbus/LICENSE.GPLv2
cp LICENSE.GPLv3 %{buildroot}/usr/share/package-licenses/qtserialbus/LICENSE.GPLv3
cp LICENSE.LGPLv3 %{buildroot}/usr/share/package-licenses/qtserialbus/LICENSE.LGPLv3
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/canbusutil

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qcanbusdevice_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qcanbusdeviceinfo_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbus_symbols_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbusadu_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbusclient_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbuscommevent_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbusdevice_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbusrtuserialmaster_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbusrtuserialslave_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbusserver_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbustcpclient_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qmodbustcpserver_p.h
/usr/include/qt5/QtSerialBus/5.12.0/QtSerialBus/private/qtserialbus-config_p.h
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5SerialBus.so.5
/usr/lib64/libQt5SerialBus.so.5.12
/usr/lib64/libQt5SerialBus.so.5.12.0
/usr/lib64/qt5/plugins/canbus/libqtpassthrucanbus.so
/usr/lib64/qt5/plugins/canbus/libqtpeakcanbus.so
/usr/lib64/qt5/plugins/canbus/libqtsocketcanbus.so
/usr/lib64/qt5/plugins/canbus/libqttinycanbus.so
/usr/lib64/qt5/plugins/canbus/libqtvirtualcanbus.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtserialbus/LICENSE.FDL
/usr/share/package-licenses/qtserialbus/LICENSE.GPLv2
/usr/share/package-licenses/qtserialbus/LICENSE.GPLv3
/usr/share/package-licenses/qtserialbus/LICENSE.LGPLv3
