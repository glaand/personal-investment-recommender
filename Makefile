update-stock-info:
	@echo "Updating stock info..."
	@python backend/scripts/update_stock_info.py

run-backend:
	@echo "Running backend..."
	cd backend/api/ && flask run --host 0.0.0.0 --port 8005
