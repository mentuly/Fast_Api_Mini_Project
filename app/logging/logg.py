import logging

logging.basicConfig(level=logging.INFO)

requests_logger = logging.getLogger("requests")
requests_handler = logging.FileHandler("requests.log")
requests_formatter = logging.Formatter("%(asctime)s - %(message)s")
requests_handler.setFormatter(requests_formatter)
requests_logger.addHandler(requests_handler)


validations_logger = logging.getLogger("validations")
validations_handler = logging.FileHandler("validations.log")
validations_formatter = logging.Formatter("%(asctime)s - %(message)s")
validations_handler.setFormatter(validations_formatter)
validations_logger.addHandler(validations_handler)


general_logger = logging.getLogger("general")
general_handler = logging.FileHandler("general.log")
general_formatter = logging.Formatter("%(asctime)s - %(message)s")
general_handler.setFormatter(general_formatter)
general_logger.addHandler(general_handler)


def log_program_start():
    general_logger.info("Program started")


def log_program_stop(reason="Normal exit"):
    general_logger.info(f"Program stopped. Reason: {reason}")
