#!/bin/bash
# cronjob.sh

START=$(date +%s)
LOG_FILE="cronjob.log"
EMAIL="youremail@example.com"

{
    echo "--- Εκκίνηση εκτέλεσης: $(date) ---"
    python3 coingecko_data.py
    python3 coinwarz_data.py
    python3 coinapi_data.py
    python3 miningpoolstats_data.py
    python3 clore_rental_data.py
    python3 sentiment_analysis.py
    python3 combine_data.py
    python3 preprocess_data.py
    python3 clean_old_data.py
    python3 train_model.py
    python3 predict_real_time.py
    echo "--- Ολοκλήρωση εκτέλεσης: $(date) ---"
} >> $LOG_FILE 2>&1

END=$(date +%s)
DIFF=$((END - START))
echo "Χρόνος εκτέλεσης: $DIFF δευτερόλεπτα" >> $LOG_FILE

if grep -q "Σφάλμα" $LOG_FILE; then
    echo "Σφάλμα εντοπίστηκε!" | mail -s "Σφάλμα στο cronjob" $EMAIL
fi
