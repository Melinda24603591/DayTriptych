# Title: DayTriptych
# Author: Tai-Fang Chung
# 52685 A2 Music Composition Project
# Description: Original work expressing emotional rhythm of a day

# Project Overview
# Duration: 2:16 (136 seconds) at 92 BPM = 52 bars total
# Audio Engine: EarSketch Python API
# Sample Validation: Pre-validated audio samples only
# Genre: R&B/Funk
# Duration: ~2:16 at 92 BPM (52 bars)

# Sections:
# S1 Sleepy Morning  :  1–9   (8 bars)
# S2 Energetic AM    :  9–21  (12 bars)
# S3 Drowsy Afternoon: 21–29  (8 bars)
# TWIL Twilight      : 29–31  (2 bars)
# S4 Energetic Dinner: 31–43  (12 bars)
# S5 Distinct Night  : 43–53  (10 bars)

# Setup Section
from earsketch import *

# Audio Engine Initialization
# Technical Implementation: Initialize EarSketch engine and set global tempo
# init(): Start audio processing engine
# setTempo(): Set global BPM for entire project (92 BPM optimal for genre)
init()
setTempo(92)

# Track Routing Configuration
# Technical Implementation: Map track numbers to semantic functions using tuple unpacking
# Memory efficient: single assignment vs. individual variable declarations
# Track Assignment: t1=drums, t2=hats, t3=pads, t4=melody, t5=snare/fx, t6=crashes, t7=ghost, t8=vocals, t9=hats(hat_fill)
t1, t2, t3, t4, t5, t6, t7, t8, t9 = 1, 2, 3, 4, 5, 6, 7, 8, 9

# Audio Sample Loading and Validation
# All samples sourced from EarSketch library
DRUM_MAIN  = COMMON_LOVE_DRUMBEAT_1
HAT_TICK   = OS_CLOSEDHAT01
SNARE_CLAP = OS_SNARE01
CYM_CRASH  = MILKNSIZZ_CRASH_PAD_DEEP_SUB_BASS

# Harmonic Content: RD_POP_PADCHORD series 
PAD_SOFT_A = RD_POP_PADCHORD_1  # Primary pad layer
PAD_SOFT_B = RD_POP_PADCHORD_2  # Secondary pad layer  
PAD_SOFT_C = RD_POP_PADCHORD_3  # Tertiary pad layer

# Melodic Elements: Specialized instrumental samples
PIANO_RNBFUNK = YG_RNB_FUNK_PIANO_1  # R&B/Funk piano for melodic parts
PLUCK_POPKEY = RD_POP_KEYPLUCK_1     # Pop keyboard pluck for rhythmic elements
BELL_AFROSENSE = MILKNSIZZ_AFROSENSE_LULLABY_BELLS  # Warm afrosense lullaby bells for atmospheric parts

# Effects and Textures - Additional sample assignments
# CYM_CRASH used for riser effects and atmospheric textures
# HAT_TICK used for percussive accents and rhythmic punctuation

# Timeline Structure Definition
# Technical Implementation: Bar-based positioning using tuple unpacking
# Format: (start_bar, end_bar) - 1-indexed to match DAW convention
# Total: 52 bars across 5 sections + 1 bridge
S1_S,  S1_E  = 1, 9    # Section 1: 8 bars
S2_S,  S2_E  = 9, 21   # Section 2: 12 bars
S3_S,  S3_E  = 21, 29  # Section 3: 8 bars
TWIL_S,TWIL_E= 29, 31  # Bridge: 2 bars
S4_S,  S4_E  = 31, 43  # Section 4: 12 bars
S5_S,  S5_E  = 43, 53  # Section 5: 10 bars

# Beat Pattern Engine
# Technical Implementation: String-based rhythmic pattern notation
# Data Structure: 16-character strings represent 16th-note divisions per bar
# Format: "0" = trigger event, "-" = rest/silence
# Memory Efficiency: strings vs boolean arrays for pattern storage
# Hat Patterns - Organized by density and character
hat_sleep   = "0---0---0---0---"  # Sparse: beats 1, 5, 9, 13 only
hat_energy  = "0--0-00-0-0-00-0"  # Dense: complex syncopation pattern
hat_drowsy  = "0---0----0---0--"  # Irregular: uneven spacing
hat_dinner8 = "0-0-0-0-0-0-0-0-"  # 8th notes: consistent subdivision
hat_quiet   = "0-------------0-"  # Minimal: beats 1 and 15 only
hat_fill    = "0-00-0-000-0-0-0"  # Fill: high-density clusters

# Texture Patterns
ghost_off   = "-0-0-0-0-0-0-0-0"  # Ghost notes: off-beat emphasis

# Vocal Chop Patterns  
vox_a = "0---0-0---0---0-"  # Vocal pattern A: specific rhythm
vox_b = "0-0-0---0-0-0---"  # Vocal pattern B: variation rhythm

# Pattern Generation Function
# Technical Implementation: Closure-based pattern application
# Input: track_id, start_bar, end_bar, pattern_string
# Process: Linear iteration with makeBeat API calls
# Complexity: O(n) where n = number of bars
def hats(track, start, end, pattern):
    """Apply rhythmic pattern to specified track and time range"""
    for m in range(start, end):  # Linear iteration through measure range
        makeBeat(HAT_TICK, track, m, pattern)  # Pattern application per measure

# SECTION 1 - TECHNICAL IMPLEMENTATION
# Architecture: Delayed entrance pattern with volume automation
# Layers: pads → hats → drums → melody (staggered entry timing)
# Duration: 8 bars (S1_S to S1_E)

# EARSKETCH API FUNCTIONS REFERENCE
# fitMedia(sample, track, start, end)
# places audio sample on specified track for given time range
# sample: audio constant (e.g., PAD_SOFT_A)
# track: track number (1-8)
# start/end: bar positions (can use decimals for sub-bar precision)

# setEffect(track, effect_type, parameter, value, [start], [end_value], [end])
# Applies audio effects to track
# VOLUME + GAIN: controls track volume in decibels (dB)
# Negative values = quieter (-10dB = moderate, -60dB = very quiet)
# Optional start/end parameters create automation curves over time

# Layer 1: Pad foundation (full section duration)
fitMedia(PAD_SOFT_A, t3, S1_S, S1_E); setEffect(t3, VOLUME, GAIN, -10)

# Layer 2: Hat pattern (delayed entry: bar 5, using sparse pattern)
hats(t2, S1_S+4, S1_E, hat_sleep); setEffect(t2, VOLUME, GAIN, -16)

# Layer 3: Drum pattern (delayed entry: bar 7)
fitMedia(DRUM_MAIN, t1, S1_S+6, S1_E); setEffect(t1, VOLUME, GAIN, -8)

# Layer 4: Melody accent (1-bar duration, fractional positioning: bar 8.5)
fitMedia(PIANO_RNBFUNK, t4, S1_S+7.5, S1_S+8.5); setEffect(t4, VOLUME, GAIN, -10)  

# Volume Automation: Ramp pad volume for section transition (-10dB to -6dB over 1 bar)
setEffect(t3, VOLUME, GAIN, -10, S1_E-1, -6, S1_E)

# Transition Element: Crash accent (0.5 bar duration)
fitMedia(CYM_CRASH, t6, S1_E, S1_E+0.5)

# S2: Energetic AM
fitMedia(DRUM_MAIN, t1, S2_S, S2_E); setEffect(t1, VOLUME, GAIN, -2)
fitMedia(PAD_SOFT_B, t3, S2_S, S2_E); setEffect(t3, VOLUME, GAIN, -6)
hats(t2, S2_S, S2_E, hat_energy)
for m in range(S2_S, S2_E, 4):
    fitMedia(PLUCK_POPKEY, t4, m+0.5, m+1.0)  # Pop keyboard pluck rhythmic pattern
    fitMedia(PLUCK_POPKEY, t4, m+2.5, m+3.0)
setEffect(t4, VOLUME, GAIN, -6)

# makeBeat API FUNCTION REFERENCE
# makeBeat(sample, track, measure, pattern)
# Creates rhythmic patterns using 16th-note string notation
# sample: audio constant for percussion sounds (e.g., SNARE_CLAP)
# track: track number (1-8)
# measure: specific bar number
# pattern: 16-character string ("0" = hit, "-" = rest)
# Unlike fitMedia which places continuous audio, makeBeat creates rhythmic hits

for m in range(S2_S, S2_E):
    makeBeat(SNARE_CLAP, t5, m, "----0-------0---")
setEffect(t5, VOLUME, GAIN, -12)
for m in range(S2_S, S2_E, 8):
    hats(t9, m+3, m+4, hat_fill)
fitMedia(CYM_CRASH, t6, S2_E-2, S2_E); setEffect(t6, VOLUME, GAIN, -12)  # Crash cymbal riser effect for section transition

# S3: Drowsy Afternoon
fitMedia(PAD_SOFT_C, t3, S3_S, S3_E); setEffect(t3, VOLUME, GAIN, -8)
fitMedia(DRUM_MAIN, t1, S3_S, S3_E);  setEffect(t1, VOLUME, GAIN, -8)
hats(t2, S3_S, S3_E, hat_drowsy);     setEffect(t2, VOLUME, GAIN, -14)
for m in range(S3_S, S3_E, 6):
    fitMedia(BELL_AFROSENSE, t4, m+0.5, m+1.5)  # Warm afrosense lullaby bells for drowsy atmosphere
setEffect(t4, VOLUME, GAIN, -8)
hats(t7, S3_S, S3_E, ghost_off); setEffect(t7, VOLUME, GAIN, -18)
setEffect(t1, VOLUME, GAIN, -8,  S3_E-2, -14, S3_E)
setEffect(t2, VOLUME, GAIN, -14, S3_E-2, -20, S3_E)
setEffect(t3, VOLUME, GAIN, -8,  S3_E-2, -6,  S3_E)

# TWILIGHT: 2-bar airy bridge
fitMedia(PAD_SOFT_C, t3, TWIL_S, TWIL_E); setEffect(t3, VOLUME, GAIN, -8)
fitMedia(CYM_CRASH, t6, TWIL_S, TWIL_E); setEffect(t6, VOLUME, GAIN, -14)  # Sustained crash for atmospheric bridge texture
makeBeat(HAT_TICK, t5, TWIL_S+1, "0---------------"); setEffect(t5, VOLUME, GAIN, -18)  # Single percussive accent for bridge punctuation

# S4: Energetic Dinner (warm energy; t4 is off-beat piano, softer)
fitMedia(DRUM_MAIN, t1, S4_S, S4_E); setEffect(t1, VOLUME, GAIN, -4)
fitMedia(PAD_SOFT_B, t3, S4_S, S4_E); setEffect(t3, VOLUME, GAIN, -6)
hats(t2, S4_S, S4_E, hat_dinner8); setEffect(t2, VOLUME, GAIN, -10)
for m in range(S4_S+3, S4_E, 8):
    hats(t9, m, m+1, hat_fill)
for m in range(S4_S, S4_E, 4):
    fitMedia(PIANO_RNBFUNK, t4, m+0.5, m+1.0)  # R&B/Funk piano off-beat pattern
setEffect(t4, VOLUME, GAIN, -8)
mid = S4_S + ((S4_E - S4_S)//2) - 1
makeBeat(HAT_TICK, t8, mid,   vox_a)   # Percussive pattern A for rhythmic texture
makeBeat(HAT_TICK, t8, mid+1, vox_b)
setEffect(t8, VOLUME, GAIN, -12)
setEffect(t1, VOLUME, GAIN, -4,  S4_E-2, -8,  S4_E)
setEffect(t9, VOLUME, GAIN, -10, S4_E-2, -16, S4_E)
setEffect(t3, VOLUME, GAIN, -6,  S4_E-2, -8,  S4_E)

# S5: Distinct Night (half-time breathing; long bells; strong fade)
fitMedia(PAD_SOFT_C, t3, S5_S, S5_E); setEffect(t3, VOLUME, GAIN, -10)
for m in range(S5_S, S5_E):
    if (m - S5_S) % 2 == 0:
        fitMedia(DRUM_MAIN, t1, m, m+1)
setEffect(t1, VOLUME, GAIN, -12)
for m in range(S5_S, S5_E):
    makeBeat(HAT_TICK, t2, m, "0--0----0--0----")
setEffect(t2, VOLUME, GAIN, -16)
for m in range(S5_S, S5_E, 4):
    fitMedia(BELL_AFROSENSE, t4, m+0.75, m+2.5)  # Extended afrosense bells for night ambience
setEffect(t4, VOLUME, GAIN, -10)
for m in range(S5_S+2, S5_E, 4):
    makeBeat(HAT_TICK, t5, m, "0---------------")  # Sparse percussive accents for night atmosphere
setEffect(t5, VOLUME, GAIN, -18)
setEffect(t3, VOLUME, GAIN, -10, S5_E-2, -18, S5_E)
setEffect(t2, VOLUME, GAIN, -16, S5_E-2, -60, S5_E)
setEffect(t1, VOLUME, GAIN, -12, S5_E-1, -60, S5_E)

finish()
