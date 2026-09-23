from typing import List, Optional, Dict, TypedDict


class Student(TypedDict):
    name: str
    score: int


class GradeStats(TypedDict):
    average: float
    count: int
    max: int
    min: int

# ========== 原始代码（无类型注解）==========
def calculate_average(scores:List[int])->Optional[float]:
    """计算成绩列表的平均分"""
    if not scores:
        return None
    return sum(scores) / len(scores)

def get_student_info(student_id: str, students_db: Dict[str, Student]) -> Optional[Student]:
    """根据学号查找学生信息"""
    return students_db.get(student_id)

def process_grades(grade_data: List[Student]) -> GradeStats:
    """处理成绩数据，返回统计结果"""
    if not grade_data:
        return {"average": 0.0, "count": 0, "max": 0, "min": 0}
    total = 0
    count = 0
    for student in grade_data:
        total += student["score"]
        count += 1
    return {
        "average": total / count,
        "count": count,
        "max": max(s["score"] for s in grade_data),
        "min": min(s["score"] for s in grade_data),
    }

def format_report(stats: Optional[GradeStats], title: str) -> str:
    """格式化统计报告"""
    if stats is None:
        return "无数据"
    report = f"=== {title} ===\n"
    report += f"人数: {stats['count']}\n"
    report += f"平均分: {stats['average']:.2f}\n"
    report += f"最高分: {stats['max']}\n"
    report += f"最低分: {stats['min']}\n"
    return report

# 测试数据
students: List[Student] = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 88},
    {"name": "Charlie", "score": 92},
]
scores:List[int] = [95, 88, 92]
student_db: Dict[str, Student] = {"S001": {"name": "Alice", "score": 95}}

avg = calculate_average(scores)
info = get_student_info("S001", student_db)
stats = process_grades(students)
report = format_report(stats, "成绩报告")
print(report)