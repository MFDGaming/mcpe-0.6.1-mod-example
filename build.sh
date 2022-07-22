#!/usr/bin/env sh

CLANG=/usr/lib/android-ndk/toolchains/llvm/prebuilt/linux-x86_64/bin/armv7a-linux-androideabi21-clang
OBJDUMP=/usr/lib/android-ndk/toolchains/arm-linux-androideabi-4.9/prebuilt/linux-x86_64/bin/arm-linux-androideabi-objdump

$CLANG -mthumb force_creative.s -o force_creative

python3 ./build.py
