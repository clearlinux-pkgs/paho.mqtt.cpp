#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : paho.mqtt.cpp
Version  : 1.1
Release  : 4
URL      : https://github.com/eclipse/paho.mqtt.cpp/archive/v1.1/paho.mqtt.cpp-1.1.tar.gz
Source0  : https://github.com/eclipse/paho.mqtt.cpp/archive/v1.1/paho.mqtt.cpp-1.1.tar.gz
Summary  : MQTT CPP Client
Group    : Development/Tools
License  : BSD-3-Clause EPL-1.0
Requires: paho.mqtt.cpp-lib = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cppunit-dev
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : openssl-dev
BuildRequires : paho.mqtt.c-dev

%description
The Paho MQTT CPP Client is a fully fledged MQTT client written in ANSI standard C++ 11.

%package dev
Summary: dev components for the paho.mqtt.cpp package.
Group: Development
Requires: paho.mqtt.cpp-lib = %{version}-%{release}
Provides: paho.mqtt.cpp-devel = %{version}-%{release}
Requires: paho.mqtt.cpp = %{version}-%{release}

%description dev
dev components for the paho.mqtt.cpp package.


%package lib
Summary: lib components for the paho.mqtt.cpp package.
Group: Libraries

%description lib
lib components for the paho.mqtt.cpp package.


%prep
%setup -q -n paho.mqtt.cpp-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571350378
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1571350378
rm -rf %{buildroot}
pushd clr-build
%make_install prefix=/usr PAHO_C_LIB_DIR=${RPM_BUILD_ROOT}/usr/lib PAHO_C_INC_DIR=${RPM_BUILD_ROOT}/usr/include
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/mqtt/async_client.h
/usr/include/mqtt/buffer_ref.h
/usr/include/mqtt/buffer_view.h
/usr/include/mqtt/callback.h
/usr/include/mqtt/client.h
/usr/include/mqtt/connect_options.h
/usr/include/mqtt/delivery_token.h
/usr/include/mqtt/disconnect_options.h
/usr/include/mqtt/exception.h
/usr/include/mqtt/iaction_listener.h
/usr/include/mqtt/iasync_client.h
/usr/include/mqtt/iclient_persistence.h
/usr/include/mqtt/message.h
/usr/include/mqtt/properties.h
/usr/include/mqtt/response_options.h
/usr/include/mqtt/server_response.h
/usr/include/mqtt/ssl_options.h
/usr/include/mqtt/string_collection.h
/usr/include/mqtt/subscribe_options.h
/usr/include/mqtt/thread_queue.h
/usr/include/mqtt/token.h
/usr/include/mqtt/topic.h
/usr/include/mqtt/types.h
/usr/include/mqtt/will_options.h
/usr/lib/cmake/PahoMqttCpp/FindPahoMqttC.cmake
/usr/lib/cmake/PahoMqttCpp/PahoMqttCppConfig.cmake
/usr/lib/cmake/PahoMqttCpp/PahoMqttCppConfigVersion.cmake
/usr/lib/cmake/PahoMqttCpp/PahoMqttCppTargets-relwithdebinfo.cmake
/usr/lib/cmake/PahoMqttCpp/PahoMqttCppTargets.cmake
/usr/lib64/libpaho-mqttpp3.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpaho-mqttpp3.so.1
/usr/lib64/libpaho-mqttpp3.so.1.1.0
