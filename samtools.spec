Summary:	Efficient utilities on manipulating alignments in the SAM format
#Summary(pl.UTF-8):	-
Name:		samtools
Version:	0.1.18
Release:	1
License:	MIT
Group:		Applications/Science
Source0:	http://sourceforge.net/projects/samtools/files/%{name}-%{version}.tar.bz2
# Source0-md5:	71dab132e21c0766f0de84c2371a9157
URL:		http://samtools.sourceforge.net/
BuildRequires:	zlib-devel >= 1.2.2.1
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SAM (Sequence Alignment/Map) is a flexible generic format for storing
nucleotide sequence alignment. SAM tools provide efficient utilities
on manipulating alignments in the SAM format.

#%description -l pl.UTF-8

%prep
%setup -q

%{__sed} -i -e 's|/software/bin/python|%{_bindir}/python|' misc/varfilter.py

%build
%{__make} \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags}"

%{__make} razip \
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

install -p razip samtools bcftools/bcftools $RPM_BUILD_ROOT%{_bindir}
install -p misc/*.pl misc/*.py $RPM_BUILD_ROOT%{_bindir}
install -p misc/{maq2sam-*,md5fa,seqtk,wgsim} $RPM_BUILD_ROOT%{_bindir}

install -p samtools.1 $RPM_BUILD_ROOT%{_mandir}/man1

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS bcftools/README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/samtools.1*
%{_examplesdir}/%{name}-%{version}
