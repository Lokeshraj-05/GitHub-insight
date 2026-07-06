import {

    PieChart,
    Pie,
    Tooltip,
    Cell

} from "recharts";

export default function SkillChart({

    skills

}) {

    const data =
        Object.entries(skills)
        .map(([k,v])=>({

            name:k,
            value:v

        }));

    return (

        <div>

            <h2>
                Skill Distribution
            </h2>

            <PieChart
                width={400}
                height={300}
            >

                <Pie
                    data={data}
                    dataKey="value"
                    outerRadius={100}
                    label
                />

                <Tooltip/>

            </PieChart>

        </div>
    );
}