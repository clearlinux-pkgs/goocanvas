#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : goocanvas
Version  : 2.0.4
Release  : 13
URL      : https://download.gnome.org/sources/goocanvas/2.0/goocanvas-2.0.4.tar.xz
Source0  : https://download.gnome.org/sources/goocanvas/2.0/goocanvas-2.0.4.tar.xz
Summary  : A GTK+ canvas widget using cairo
Group    : Development/Tools
License  : LGPL-2.0
Requires: goocanvas-data = %{version}-%{release}
Requires: goocanvas-lib = %{version}-%{release}
Requires: goocanvas-license = %{version}-%{release}
Requires: goocanvas-locales = %{version}-%{release}
Requires: goocanvas-python = %{version}-%{release}
Requires: goocanvas-python3 = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : glibc-bin
BuildRequires : gtk+-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(pygobject-3.0)

%description
Welcome to GooCanvas
====================
(a cairo-based canvas widget for GTK+)

%package data
Summary: data components for the goocanvas package.
Group: Data

%description data
data components for the goocanvas package.


%package dev
Summary: dev components for the goocanvas package.
Group: Development
Requires: goocanvas-lib = %{version}-%{release}
Requires: goocanvas-data = %{version}-%{release}
Provides: goocanvas-devel = %{version}-%{release}
Requires: goocanvas = %{version}-%{release}

%description dev
dev components for the goocanvas package.


%package doc
Summary: doc components for the goocanvas package.
Group: Documentation

%description doc
doc components for the goocanvas package.


%package lib
Summary: lib components for the goocanvas package.
Group: Libraries
Requires: goocanvas-data = %{version}-%{release}
Requires: goocanvas-license = %{version}-%{release}

%description lib
lib components for the goocanvas package.


%package license
Summary: license components for the goocanvas package.
Group: Default

%description license
license components for the goocanvas package.


%package locales
Summary: locales components for the goocanvas package.
Group: Default

%description locales
locales components for the goocanvas package.


%package python
Summary: python components for the goocanvas package.
Group: Default
Requires: goocanvas-python3 = %{version}-%{release}

%description python
python components for the goocanvas package.


%package python3
Summary: python3 components for the goocanvas package.
Group: Default
Requires: python3-core

%description python3
python3 components for the goocanvas package.


%prep
%setup -q -n goocanvas-2.0.4
cd %{_builddir}/goocanvas-2.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586232192
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1586232192
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/goocanvas
cp %{_builddir}/goocanvas-2.0.4/COPYING %{buildroot}/usr/share/package-licenses/goocanvas/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
%make_install
%find_lang goocanvas2

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GooCanvas-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/goocanvas-2.0/goocanvas.h
/usr/include/goocanvas-2.0/goocanvasellipse.h
/usr/include/goocanvas-2.0/goocanvasenumtypes.h
/usr/include/goocanvas-2.0/goocanvasgrid.h
/usr/include/goocanvas-2.0/goocanvasgroup.h
/usr/include/goocanvas-2.0/goocanvasimage.h
/usr/include/goocanvas-2.0/goocanvasitem.h
/usr/include/goocanvas-2.0/goocanvasitemmodel.h
/usr/include/goocanvas-2.0/goocanvasitemsimple.h
/usr/include/goocanvas-2.0/goocanvasmarshal.h
/usr/include/goocanvas-2.0/goocanvaspath.h
/usr/include/goocanvas-2.0/goocanvaspolyline.h
/usr/include/goocanvas-2.0/goocanvasrect.h
/usr/include/goocanvas-2.0/goocanvasstyle.h
/usr/include/goocanvas-2.0/goocanvastable.h
/usr/include/goocanvas-2.0/goocanvastext.h
/usr/include/goocanvas-2.0/goocanvasutils.h
/usr/include/goocanvas-2.0/goocanvaswidget.h
/usr/lib64/libgoocanvas-2.0.so
/usr/lib64/pkgconfig/goocanvas-2.0.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/goocanvas2/GooCanvas.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasEllipse.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasEllipseModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasGrid.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasGridModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasGroup.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasGroupModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasImage.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasImageModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasItem.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasItemModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasItemModelSimple.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasItemSimple.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasPath.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasPathModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasPolyline.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasPolylineModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasRect.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasRectModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasStyle.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasTable.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasTableModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasText.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasTextModel.html
/usr/share/gtk-doc/html/goocanvas2/GooCanvasWidget.html
/usr/share/gtk-doc/html/goocanvas2/api-index-2.0.1.html
/usr/share/gtk-doc/html/goocanvas2/api-index-2.0.2.html
/usr/share/gtk-doc/html/goocanvas2/api-index-full.html
/usr/share/gtk-doc/html/goocanvas2/ch01.html
/usr/share/gtk-doc/html/goocanvas2/ch02.html
/usr/share/gtk-doc/html/goocanvas2/ch03.html
/usr/share/gtk-doc/html/goocanvas2/ch04.html
/usr/share/gtk-doc/html/goocanvas2/ch05.html
/usr/share/gtk-doc/html/goocanvas2/deprecated-api-index.html
/usr/share/gtk-doc/html/goocanvas2/goocanvas-architecture.html
/usr/share/gtk-doc/html/goocanvas2/goocanvas-coordinates.html
/usr/share/gtk-doc/html/goocanvas2/goocanvas-creating-items.html
/usr/share/gtk-doc/html/goocanvas2/goocanvas-model-view-canvas.html
/usr/share/gtk-doc/html/goocanvas2/goocanvas-overview.html
/usr/share/gtk-doc/html/goocanvas2/goocanvas-simple-canvas.html
/usr/share/gtk-doc/html/goocanvas2/goocanvas-wysiwyg.html
/usr/share/gtk-doc/html/goocanvas2/goocanvas2-GooCanvas-Types.html
/usr/share/gtk-doc/html/goocanvas2/goocanvas2.devhelp2
/usr/share/gtk-doc/html/goocanvas2/home.png
/usr/share/gtk-doc/html/goocanvas2/index.html
/usr/share/gtk-doc/html/goocanvas2/left-insensitive.png
/usr/share/gtk-doc/html/goocanvas2/left.png
/usr/share/gtk-doc/html/goocanvas2/right-insensitive.png
/usr/share/gtk-doc/html/goocanvas2/right.png
/usr/share/gtk-doc/html/goocanvas2/style.css
/usr/share/gtk-doc/html/goocanvas2/up-insensitive.png
/usr/share/gtk-doc/html/goocanvas2/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgoocanvas-2.0.so.9
/usr/lib64/libgoocanvas-2.0.so.9.3.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/goocanvas/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f goocanvas2.lang
%defattr(-,root,root,-)

