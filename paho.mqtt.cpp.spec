#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v16
# autospec commit: b858a2a99030
#
Name     : paho.mqtt.cpp
Version  : 1.4.1
Release  : 9
URL      : https://github.com/eclipse/paho.mqtt.cpp/archive/v1.4.1/paho.mqtt.cpp-1.4.1.tar.gz
Source0  : https://github.com/eclipse/paho.mqtt.cpp/archive/v1.4.1/paho.mqtt.cpp-1.4.1.tar.gz
Summary  : MQTT CPP Client
Group    : Development/Tools
License  : BSD-3-Clause EPL-1.0 EPL-2.0
Requires: paho.mqtt.cpp-lib = %{version}-%{release}
Requires: paho.mqtt.cpp-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cppunit-dev
BuildRequires : doxygen
BuildRequires : glibc-dev
BuildRequires : openssl-dev
BuildRequires : paho.mqtt.c-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
Requires: paho.mqtt.cpp-license = %{version}-%{release}

%description lib
lib components for the paho.mqtt.cpp package.


%package license
Summary: license components for the paho.mqtt.cpp package.
Group: Default

%description license
license components for the paho.mqtt.cpp package.


%prep
%setup -q -n paho.mqtt.cpp-1.4.1
cd %{_builddir}/paho.mqtt.cpp-1.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720817069
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}  prefix=/usr PAHO_C_LIB_DIR=${RPM_BUILD_ROOT}/usr/lib PAHO_C_INC_DIR=${RPM_BUILD_ROOT}/usr/include
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1720817069
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/paho.mqtt.cpp
cp %{_builddir}/paho.mqtt.cpp-%{version}/edl-v10 %{buildroot}/usr/share/package-licenses/paho.mqtt.cpp/03b5669874cbaabe055c6d130446ade35b3f8c65 || :
cp %{_builddir}/paho.mqtt.cpp-%{version}/epl-v20 %{buildroot}/usr/share/package-licenses/paho.mqtt.cpp/b086d72d0fe9af38418dab524fe76eea3cb1eec3 || :
export GOAMD64=v2
GOAMD64=v2
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
/usr/include/mqtt/create_options.h
/usr/include/mqtt/delivery_token.h
/usr/include/mqtt/disconnect_options.h
/usr/include/mqtt/exception.h
/usr/include/mqtt/export.h
/usr/include/mqtt/iaction_listener.h
/usr/include/mqtt/iasync_client.h
/usr/include/mqtt/iclient_persistence.h
/usr/include/mqtt/message.h
/usr/include/mqtt/platform.h
/usr/include/mqtt/properties.h
/usr/include/mqtt/response_options.h
/usr/include/mqtt/server_response.h
/usr/include/mqtt/ssl_options.h
/usr/include/mqtt/string_collection.h
/usr/include/mqtt/subscribe_options.h
/usr/include/mqtt/thread_queue.h
/usr/include/mqtt/token.h
/usr/include/mqtt/topic.h
/usr/include/mqtt/topic_matcher.h
/usr/include/mqtt/types.h
/usr/include/mqtt/will_options.h
/usr/lib/cmake/PahoMqttCpp/PahoMqttCppConfig.cmake
/usr/lib/cmake/PahoMqttCpp/PahoMqttCppConfigVersion.cmake
/usr/lib/cmake/PahoMqttCpp/PahoMqttCppTargets-relwithdebinfo.cmake
/usr/lib/cmake/PahoMqttCpp/PahoMqttCppTargets.cmake
/usr/lib64/libpaho-mqttpp3.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpaho-mqttpp3.so.1
/usr/lib64/libpaho-mqttpp3.so.1.4.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/paho.mqtt.cpp/03b5669874cbaabe055c6d130446ade35b3f8c65
/usr/share/package-licenses/paho.mqtt.cpp/b086d72d0fe9af38418dab524fe76eea3cb1eec3
