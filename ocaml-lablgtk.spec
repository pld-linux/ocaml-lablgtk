#
# Conditional build:
# _without_gl		- without lablgtkgl
# _without_gnome	- without lablgnome
# _without_glade	- without lablglade
#
%if 0%{?_without_glade:1}%{?_without_gnome:1}
%define _without_glgn 1
%endif
%define _snap 20030423
Summary:	GTK+ binding for OCaml
Summary(pl):	Wi�zania GTK+ dla OCamla
Name:		ocaml-lablgtk
Version:	1.3.1
Release:	0.%{_snap}.1
License:	LGPL w/ linking exceptions
Group:		Libraries
Source0:	http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/lablgtk2-%{_snap}.tar.gz
# Source0-md5:	f20de46a7de7790e2345f18bc6759615
URL:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/lablgtk.html
%{!?_without_gnome:BuildRequires:	libgnomecanvas-devel}
BuildRequires:	gtk+2-devel
BuildRequires:	librsvg-devel >= 2.0
%{!?_without_gl:BuildRequires:	gtkglarea-devel}
%{!?_without_glade:BuildRequires:	libglade2-devel}
BuildRequires:	libxml-devel
BuildRequires:	ocaml-camlp4 >= 3.04-7
%{!?_without_gl:BuildRequires:	ocaml-lablgl-devel}
%requires_eq	ocaml-runtime
Obsoletes:	lablgtk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ binding for OCaml. This package contains files needed to run
bytecode OCaml programs using LablGtk.

%description -l pl
Wi�zania GTK+ dla OCamla. Pakiet ten zawiera binaria potrzebne do
uruchamiania program�w u�ywaj�cych LablGtk.

%package devel
Summary:	GTK+ binding for OCaml - development part
Summary(pl):	Wi�zania GTK+ dla OCamla - cze�� programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
%requires_eq	ocaml-lablgl-devel
Obsoletes:	lablgtk-examples

%description devel
GTK+ binding for OCaml. This package contains files needed to develop
OCaml programs using LablGtk.

%description devel -l pl
Wi�zania GTK+ dla OCamla. Pakiet ten zawiera pliki niezb�dne do
tworzenia program�w u�ywaj�cych LablGtk.

%package gnome
Summary:	GTK+ binding for OCaml - GNOME support
Summary(pl):	Wi�zania GTK+ dla OCamla - wsparcie dla GNOME
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description gnome
GTK+ binding for OCaml, GNOME support. This package contains files
needed to run bytecode OCaml programs using LablGtk-GNOME.

%description gnome -l pl
Wi�zania GTK+ dla OCamla, wsparcie dla GNOME. Pakiet ten zawiera
binaria potrzebne do uruchamiania program�w u�ywaj�cych LablGtk-GNOME.

%package gnome-devel
Summary:	GTK+ binding for OCaml - GNOME support, development part
Summary(pl):	Wi�zania GTK+ dla OCamla - wsparcie dla GNOME, cz�� programistyczna
Group:		Development/Libraries
Requires:	%{name}-gnome = %{version}-%{release}
%requires_eq	ocaml

%description gnome-devel
GTK+ binding for OCaml, GNOME support. This package contains files
needed to develop OCaml programs using LablGtk-GNOME.

%description gnome-devel -l pl
Wi�zania GTK+ dla OCamla, wsparcie dla GNOME. Pakiet ten zawiera pliki
niezb�dne do tworzenia program�w u�ywaj�cych LablGtk-GNOME.

%package glade
Summary:	GTK+ binding for OCaml - Glade support
Summary(pl):	Wi�zania GTK+ dla OCamla - wsparcie dla Glade
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description glade
GTK+ binding for OCaml, Glade support. This package contains files
needed to run bytecode OCaml programs using LablGtk-Glade.

%description glade -l pl
Wi�zania GTK+ dla OCamla, wsparcie dla Glade. Pakiet ten zawiera
binaria potrzebne do uruchamiania program�w u�ywaj�cych LablGtk-Glade.

%package glade-devel
Summary:	GTK+ binding for OCaml - Glade support, development part
Summary(pl):	Wi�zania GTK+ dla OCamla - wsparcie dla Glade, cz�� programistyczna
Group:		Development/Libraries
Requires:	%{name}-glade = %{version}-%{release}
%requires_eq	ocaml

%description glade-devel
GTK+ binding for OCaml, Glade support. This package contains files
needed to develop OCaml programs using LablGtk-Glade.

%description glade-devel -l pl
Wi�zania GTK+ dla OCamla, wsparcie dla Glade. Pakiet ten zawiera pliki
niezb�dne do tworzenia program�w u�ywaj�cych LablGtk-Glade.

%package rsvg
Summary:	GTK+ binding for OCaml - RSVG support
Summary(pl):	Wi�zania GTK+ dla OCamla - wsparcie dla RSVG
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime

%description rsvg
GTK+ binding for OCaml, RSVG support. This package contains files
needed to run bytecode OCaml programs using LablGtk-RSVG.

%description rsvg -l pl
Wi�zania GTK+ dla OCamla, wsparcie dla RSVG. Pakiet ten zawiera
binaria potrzebne do uruchamiania program�w u�ywaj�cych LablGtk-RSVG.

%package rsvg-devel
Summary:	GTK+ binding for OCaml - RSVG support, development part
Summary(pl):	Wi�zania GTK+ dla OCamla - wsparcie dla RSVG, cz�� programistyczna
Group:		Development/Libraries
Requires:	%{name}-rsvg = %{version}-%{release}
%requires_eq	ocaml

%description rsvg-devel
GTK+ binding for OCaml, RSVG support. This package contains files
needed to develop OCaml programs using LablGtk-RSVG.

%description rsvg-devel -l pl
Wi�zania GTK+ dla OCamla, wsparcie dla RSVG. Pakiet ten zawiera pliki
niezb�dne do tworzenia program�w u�ywaj�cych LablGtk-RSVG.

%package gl
Summary:	GTK+ binding for OCaml - GtkGL support
Summary(pl):	Wi�zania GTK+ dla OCamla - wsparcie dla GtkGL
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml-runtime
%requires_eq	ocaml-lablgl

%description gl
GTK+ binding for OCaml, GtkGL support. This package contains files
needed to run bytecode OCaml programs using LablGtk-GtkGL.

%description gl -l pl
Wi�zania GTK+ dla OCamla, wsparcie dla GtkGL. Pakiet ten zawiera
binaria potrzebne do uruchamiania program�w u�ywaj�cych LablGtk-GtkGL.

%package gl-devel
Summary:	GTK+ binding for OCaml - GtkGL support, development part
Summary(pl):	Wi�zania GTK+ dla OCamla - wsparcie dla GtkGL, cz�� programistyczna
Group:		Development/Libraries
Requires:	%{name}-gl = %{version}-%{release}
%requires_eq	ocaml
%requires_eq	ocaml-lablgl-devel

%description gl-devel
GTK+ binding for OCaml, GtkGL support. This package contains files
needed to develop OCaml programs using LablGtk-GtkGL.

%description gl-devel -l pl
Wi�zania GTK+ dla OCamla, wsparcie dla GtkGL. Pakiet ten zawiera pliki
niezb�dne do tworzenia program�w u�ywaj�cych LablGtk-GtkGL.

%package toplevel
Summary:	GTK+ binding for OCaml - interactive system
Summary(pl):	Wi�zania GTK+ dla OCamla - system interaktywny
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
%requires_eq	ocaml

%description toplevel
GTK+ binding for OCaml. GNOME and Glade support is included. This
package contains OCaml toplevel interactive system linked with
lablgtk.

%description toplevel -l pl
Wi�zania GTK+ dla OCamla. Wsparcie dla GNOME i Glade jest do��czone.
Pakiet ten zawiera system interaktywny OCamla zlinkowany z lablgtk.

%prep
%setup -q -n lablgtk2

%build
%{__make} configure \
	CC="%{__cc} %{rpmcflags} -fPIC" \
	USE_CC=1 \
	%{!?_without_gnome:USE_GNOMECANVAS=1} \
	%{!?_without_glade:USE_GLADE=1} \
	%{!?_without_gl:USE_GL=1} \
	USE_RSVG=1

%{__make} all opt \
	LABLGLDIR=%{_libdir}/ocaml/lablgl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/stublibs}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk \
	DLLDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs \
	LIBDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# .mli files stay, they are the only documentation, but .ml go
rm -f $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk/*.ml
gzip -9nf $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk/*.mli
mv $RPM_BUILD_ROOT%{_libdir}/ocaml/lablgtk/*.gz .

# make METAs for findlib
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/labl{gtk,gnomecanvas,glade,gtkgl,rsvg}
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/lablgtk/META <<EOF
# Specifications for the "lablgtk" library:
requires = ""
version = "%{version}"
directory = "+lablgtk"
archive(byte) = "lablgtk.cma gtkInit.cmo"
archive(native) = "lablgtk.cmxa gtkInit.cmx"
linkopts = ""
EOF

for f in gnomecanvas glade gtkgl rsvg ; do
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/labl$f/META <<EOF
# Specifications for the "lablgtk" library:
requires = "lablgtk"
version = "%{version}"
directory = "+lablgtk"
archive(byte) = "labl$f.cma"
archive(native) = "labl$f.cmxa"
linkopts = ""
EOF
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%dir %{_libdir}/ocaml/lablgtk
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk2.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk/g[BCDELMOPRTUWadp]*.cm*
%{_libdir}/ocaml/lablgtk/glib.cm*
%{_libdir}/ocaml/lablgtk/gobject.cm*
%{_libdir}/ocaml/lablgtk/gtk.cm*
%{_libdir}/ocaml/lablgtk/pango.cm*
%{_libdir}/ocaml/lablgtk/gtk[ABDEILMNPRSTW]*.cm*
# hmm.. where did xml_lexer go?
#%%{_libdir}/ocaml/lablgtk/x*.cm*
%{_libdir}/ocaml/lablgtk/*.[ho]
%{_libdir}/ocaml/lablgtk/lablgtk.*
%{_libdir}/ocaml/lablgtk/liblablgtk2.*
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/varcc
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/lablgtk

%if 0%{!?_without_gnome:1}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgnomecanvas.so

%files gnome-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk/*Canvas*.cm*
%{_libdir}/ocaml/lablgtk/lablgnomecanvas.*
%{_libdir}/ocaml/lablgtk/liblablgnomecanvas.*
%{_libdir}/ocaml/site-lib/lablgnomecanvas
%endif

%if 0%{!?_without_glade:1}
%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablglade2.so

%files glade-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgladecc2
%{_libdir}/ocaml/lablgtk/glade.cm*
%{_libdir}/ocaml/lablgtk/lablglade.*
%{_libdir}/ocaml/lablgtk/liblablglade2.*
%{_libdir}/ocaml/site-lib/lablglade
%endif

%if 0%{!?_without_gl:1}
%files gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtkgl2.so

%files gl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk/glGtk.cm*
%{_libdir}/ocaml/lablgtk/lablgtkgl.*
%{_libdir}/ocaml/lablgtk/liblablgtkgl2.*
%{_libdir}/ocaml/site-lib/lablgtkgl
%endif

%files rsvg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablrsvg.so

%files rsvg-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk/rsvg.cm*
%{_libdir}/ocaml/lablgtk/lablrsvg.*
%{_libdir}/ocaml/lablgtk/liblablrsvg.*
%{_libdir}/ocaml/site-lib/lablrsvg

%files toplevel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgtk2
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/lablgtktop
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/lablgtktop_t
