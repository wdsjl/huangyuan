# 结局判定系统

init python:
    def check_ending():
        if transcendence >= 80:
            return "ending_transcendence"
        elif authority >= 80:
            return "ending_authority"
        elif logic >= 80:
            return "ending_logic"
        elif humanity >= 80:
            return "ending_humanity"
        else:
            return "ending_default"
