# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['课外需求\\Word文档集词云生成系统.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Windows/Fonts/simhei.ttf', '.')],
    hiddenimports=['matplotlib', 'wordcloud'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Word文档集词云生成系统',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
