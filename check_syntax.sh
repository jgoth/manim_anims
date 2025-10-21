#!/bin/bash
# Script to verify all Python animation files have valid syntax

echo "Checking Python syntax for all animation files..."
echo ""

errors=0

for file in animations/**/*.py; do
    if [ -f "$file" ]; then
        if python3 -m py_compile "$file" 2>/dev/null; then
            echo "✓ $file"
        else
            echo "✗ $file - SYNTAX ERROR"
            errors=$((errors + 1))
        fi
    fi
done

echo ""
if [ $errors -eq 0 ]; then
    echo "All files passed syntax check!"
    exit 0
else
    echo "Found $errors file(s) with syntax errors"
    exit 1
fi
