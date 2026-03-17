def build_recommendation_reason(series: dict, score_breakdown: dict, profile: dict) -> str:
    liked = sorted(set(series.get("tags", [])) & set(profile.get("liked_tags", [])))
    disliked = sorted(set(series.get("tags", [])) & set(profile.get("disliked_tags", [])))
    parts = []
    if liked:
        parts.append(f"命中你偏好的标签：{', '.join(liked)}。")
    if not disliked and profile.get("disliked_tags"):
        parts.append("没有命中你明确排斥的标签。")
    if score_breakdown.get("freshness_score", 0) > 0 or score_breakdown.get("series_activity_score", 0) > 0:
        parts.append("最近更新较新且近 7 天活跃度较高。")
    if score_breakdown.get("feedback_similarity_score", 0) > 0:
        parts.append("它与您已标记喜欢的系列在题材标签上接近。")
    if not parts:
        parts.append("它在当前候选池中综合分数较高，且具备稳定更新与可接受标签匹配。")
    return " ".join(parts[:4])
