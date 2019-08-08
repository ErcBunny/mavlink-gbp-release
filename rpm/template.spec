Name:           ros-melodic-mavlink
Version:        2019.8.8
Release:        1%{?dist}
Summary:        ROS mavlink package

Group:          Development/Libraries
License:        LGPLv3
URL:            https://mavlink.io/en/
Source0:        %{name}-%{version}.tar.gz

Requires:       python-devel
Requires:       ros-melodic-catkin
BuildRequires:  cmake
BuildRequires:  python-devel
BuildRequires:  python-future
BuildRequires:  python-lxml
BuildRequires:  python-setuptools

%description
MAVLink message marshaling library. This package provides C-headers and C++11
library for both 1.0 and 2.0 versions of protocol. For pymavlink use separate
install via rosdep (python-pymavlink).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Aug 08 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.8.8-1
- Autogenerated by Bloom

* Sat Jul 06 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.7.7-1
- Autogenerated by Bloom

* Fri Jun 07 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.6.7-1
- Autogenerated by Bloom

* Mon May 20 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.5.20-1
- Autogenerated by Bloom

* Thu Apr 04 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.4.4-0
- Autogenerated by Bloom

* Sun Mar 03 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.3.3-0
- Autogenerated by Bloom

* Sat Feb 02 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.2.2-0
- Autogenerated by Bloom

* Sat Jan 12 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.1.12-0
- Autogenerated by Bloom

* Thu Jan 03 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.01.03-0
- Autogenerated by Bloom

* Thu Jan 03 2019 Vladimir Ermakov <vooon341@gmail.com> - 2019.1.3-0
- Autogenerated by Bloom

* Wed Dec 12 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.12.12-0
- Autogenerated by Bloom

* Sat Nov 10 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.11.11-0
- Autogenerated by Bloom

* Wed Oct 10 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.10.10-0
- Autogenerated by Bloom

* Mon Sep 17 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.9.17-0
- Autogenerated by Bloom

* Wed Aug 08 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.8.8-0
- Autogenerated by Bloom

* Wed Jul 18 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.7.18-0
- Autogenerated by Bloom

* Fri Jul 06 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.7.7-0
- Autogenerated by Bloom

* Wed Jun 06 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.6.6-0
- Autogenerated by Bloom

* Mon May 07 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.5.7-0
- Autogenerated by Bloom

* Sun May 06 2018 Vladimir Ermakov <vooon341@gmail.com> - 2018.5.6-0
- Autogenerated by Bloom

