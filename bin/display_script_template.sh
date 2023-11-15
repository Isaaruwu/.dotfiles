#!/bin/bash

# Fetch Traking stocks
STOCKS=("AAPL" "GOOGL" "TSLA")

echo "🚀 Stocks Variations Today: "
python3 ~/.dotfiles/bin/stock.py "${STOCKS[@]}"
