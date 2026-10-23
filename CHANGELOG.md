# Changelog

All notable changes to this project will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-10-23

### Added

- Eight themes: Islands Archipelago Dark/Light in Hard, Medium, and Soft, plus
  classic Mainland Dark/Light in Medium.
- Canonical Gruvbox Medium background as the default for Archipelago Dark and
  Archipelago Light.
- Six editor schemes covering dark/light Hard, Medium, and Soft variants.
- Shared palette generator for all eight theme variants.
- Scheme generator for the Medium and Soft editor schemes.
- Canonical Gruvbox palette across all UI surfaces and editor schemes.
- Islands UI support plus classic flat variants.

### Fixed

- Medium and Soft editor panes now use their own background instead of the
  Hard `TEXT` background from the source scheme.
- Rounded buttons no longer show a square background behind their corners.
- Inactive tool-window headers and tabs follow the Medium and Soft surfaces
  instead of falling back to the Hard near-black layer.
- Selected files remain highlighted in the Light Soft project tree instead of
  blending into the tool-window background.
