#
# Conditional build:

%bcond_with gl	# without lablgtkgl
%bcond_with gnome	# without lablgtkgnome
%bcond_with glade	# without lablgtkglade

Summary:	GTK+ binding for OCaml
Summary(pl):	Wi±zania GTK+ dla OCamla
Name:		ocaml-lablgtk
Epoch:		1
Version:	1.2.5
Release:	1
License:	LGPL w/ linking exceptions
Group:		Libraries
Source0:	http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/dist/lablgtk-%{version}.tar.gz
# Source0-md5:	92628c756d2d3e2706b59d0382f23c19
URL:		http://wwwfun.kurims.kyoto-u.ac.jp/soft/olabl/lablgtk.html
BuildRequires:	gdk-pixbuf-devel
%{?with_gnome:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel
%{?with_gl:BuildRequires:	gtkglarea1-devel >= 1.2.0}
%{?with_glade:BuildRequires:	libglade-devel}
%if %{with glade} && %{with gnome}
BuildRequires:  libglade-gnome-devel
%endif
BuildRequires:	libxml-devel
BuildRequires:	ocaml-camlp4 >= 3.04-7
%{?with_gl:BuildRequires:	ocaml-lablgl-devel}
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	lablgtk

%description
GTK+ binding for OCaml. This package contains files needed to run
bytecode OCaml programs using LablGtk.

%description -l pl
Wi±zania GTK+ dla OCamla. Pakiet ten zawiera binaria potrzebne do
uruchamiania programów u¿ywaj±cych LablGtk.

%package devel
Summary:	GTK+ binding for OCaml - development part
Summary(pl):	Wi±zania GTK+ dla OCamla - cze¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%requires_eq	ocaml
%requires_eq	ocaml-lablgl-devel
Obsoletes:	lablgtk-examples

%description devel
GTK+ binding for OCaml. This package contains files needed to develop
OCaml programs using LablGtk.

%description devel -l pl
Wi±zania GTK+ dla OCamla. Pakiet ten zawiera pliki niezbêdne do
tworzenia programów u¿ywaj±cych LablGtk.

%package gnome
Summary:	GTK+ binding for OCaml - GNOME support
Summary(pl):	Wi±zania GTK+ dla OCamla - wsparcie dla GNOME
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%requires_eq	ocaml-runtime

%description gnome
GTK+ binding for OCaml, GNOME support. This package contains files
needed to run bytecode OCaml programs using LablGtk-GNOME.

%description gnome -l pl
Wi±zania GTK+ dla OCamla, wsparcie dla GNOME. Pakiet ten zawiera
binaria potrzebne do uruchamiania programów u¿ywaj±cych LablGtk-GNOME.

%package gnome-devel
Summary:	GTK+ binding for OCaml - GNOME support, development part
Summary(pl):	Wi±zania GTK+ dla OCamla - wsparcie dla GNOME, czê¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name}-gnome = %{version}-%{release}
%requires_eq	ocaml

%description gnome-devel
GTK+ binding for OCaml, GNOME support. This package contains files
needed to develop OCaml programs using LablGtk-GNOME.

%description gnome-devel -l pl
Wi±zania GTK+ dla OCamla, wsparcie dla GNOME. Pakiet ten zawiera pliki
niezbêdne do tworzenia programów u¿ywaj±cych LablGtk-GNOME.

%package glade
Summary:	GTK+ binding for OCaml - Glade support
Summary(pl):	Wi±zania GTK+ dla OCamla - wsparcie dla Glade
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%requires_eq	ocaml-runtime

%description glade
GTK+ binding for OCaml, Glade support. This package contains files
needed to run bytecode OCaml programs using LablGtk-Glade.

%description glade -l pl
Wi±zania GTK+ dla OCamla, wsparcie dla Glade. Pakiet ten zawiera
binaria potrzebne do uruchamiania programów u¿ywaj±cych LablGtk-Glade.

%package glade-devel
Summary:	GTK+ binding for OCaml - Glade support, development part
Summary(pl):	Wi±zania GTK+ dla OCamla - wsparcie dla Glade, czê¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name}-glade = %{epoch}:%{version}-%{release}
%requires_eq	ocaml

%description glade-devel
GTK+ binding for OCaml, Glade support. This package contains files
needed to develop OCaml programs using LablGtk-Glade.

%description glade-devel -l pl
Wi±zania GTK+ dla OCamla, wsparcie dla Glade. Pakiet ten zawiera pliki
niezbêdne do tworzenia programów u¿ywaj±cych LablGtk-Glade.

%package gl
Summary:	GTK+ binding for OCaml - GtkGL support
Summary(pl):	Wi±zania GTK+ dla OCamla - wsparcie dla GtkGL
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
%requires_eq	ocaml-runtime
%requires_eq	ocaml-lablgl

%description gl
GTK+ binding for OCaml, GtkGL support. This package contains files
needed to run bytecode OCaml programs using LablGtk-GtkGL.

%description gl -l pl
Wi±zania GTK+ dla OCamla, wsparcie dla GtkGL. Pakiet ten zawiera
binaria potrzebne do uruchamiania programów u¿ywaj±cych LablGtk-GtkGL.

%package gl-devel
Summary:	GTK+ binding for OCaml - GtkGL support, development part
Summary(pl):	Wi±zania GTK+ dla OCamla - wsparcie dla GtkGL, czê¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name}-gl = %{epoch}:%{version}-%{release}
%requires_eq	ocaml
%requires_eq	ocaml-lablgl-devel

%description gl-devel
GTK+ binding for OCaml, GtkGL support. This package contains files
needed to develop OCaml programs using LablGtk-GtkGL.

%description gl-devel -l pl
Wi±zania GTK+ dla OCamla, wsparcie dla GtkGL. Pakiet ten zawiera pliki
niezbêdne do tworzenia programów u¿ywaj±cych LablGtk-GtkGL.

%package toplevel
Summary:	GTK+ binding for OCaml - interactive system
Summary(pl):	Wi±zania GTK+ dla OCamla - system interaktywny
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
%requires_eq	ocaml

%description toplevel
GTK+ binding for OCaml. GNOME and Glade support is included. This
package contains OCaml toplevel interactive system linked with
lablgtk.

%description toplevel -l pl
Wi±zania GTK+ dla OCamla. Wsparcie dla GNOME i Glade jest do³±czone.
Pakiet ten zawiera system interaktywny OCamla zlinkowany z lablgtk.

%prep
%setup -q -n lablgtk-%{version}

%build
%{__make} configure \
	CC="%{__cc} %{rpmcflags} -fPIC" \
	USE_CC=1 \
	%{?with_gnome:USE_GNOME=1} \
	%{?with_glade:USE_GLADE=1} \
	%{?with_gl:USE_GL=1}

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
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/labl{gtk,gnome,glade,gtkgl}
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/lablgtk/META <<EOF
# Specifications for the "lablgtk" library:
requires = ""
version = "%{version}"
directory = "+lablgtk"
archive(byte) = "lablgtk.cma gtkInit.cmo"
archive(native) = "lablgtk.cmxa gtkInit.cmx"
linkopts = ""
EOF

for f in gnome glade gtkgl ; do
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
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtk.so

%files devel
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%dir %{_libdir}/ocaml/lablgtk
%{_libdir}/ocaml/lablgtk/g[BCDELMOPRTUWadp]*.cm*
%{_libdir}/ocaml/lablgtk/glib.cm*
%{_libdir}/ocaml/lablgtk/gtk.cm*
%{_libdir}/ocaml/lablgtk/gtk[ABDEILMNPRSTW]*.cm*
# hmm.. where did xml_lexer go?
#%%{_libdir}/ocaml/lablgtk/x*.cm*
%{_libdir}/ocaml/lablgtk/*.[ho]
%{_libdir}/ocaml/lablgtk/lablgtk.*
%{_libdir}/ocaml/lablgtk/liblablgtk.*
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/varcc
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/lablgtk

%if %{with gnome}
%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgnome.so
%{_libdir}/ocaml/dlllablgnome.so

%files gnome-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk/gtkXmHTML.cm*
%{_libdir}/ocaml/lablgtk/gHtml.cm*
%{_libdir}/ocaml/lablgtk/lablgnome.*
%{_libdir}/ocaml/lablgtk/liblablgnome.*
%{_libdir}/ocaml/site-lib/lablgnome
%endif

%if %{with glade}
%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablglade.so
%{_libdir}/ocaml/dlllablglade.so

%files glade-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgladecc
%{_libdir}/ocaml/lablgtk/glade.cm*
%{_libdir}/ocaml/lablgtk/lablglade.*
%{_libdir}/ocaml/lablgtk/liblablglade.*
%{_libdir}/ocaml/site-lib/lablglade
%endif

%if %{with gl}
%files gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dlllablgtkgl.so
%{_libdir}/ocaml/dlllablgtkgl.so

%files gl-devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/lablgtk/glGtk.cm*
%{_libdir}/ocaml/lablgtk/lablgtkgl.*
%{_libdir}/ocaml/lablgtk/liblablgtkgl.*
%{_libdir}/ocaml/site-lib/lablgtkgl
%endif

%files toplevel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lablgtk
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/lablgtktop
%attr(755,root,root) %{_libdir}/ocaml/lablgtk/lablgtktop_t
