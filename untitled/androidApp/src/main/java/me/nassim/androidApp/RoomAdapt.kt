package me.nassim.androidApp

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ListView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class RoomAdapt(private val context: Context, private val list: ArrayList<Room>, private val rangeList: ArrayList<Range>): RecyclerView.Adapter<RoomAdapt.ViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val moduleList = LayoutInflater.from(context).inflate(R.layout.item_room, parent, false)
        return ViewHolder(moduleList)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(list[position])
    }

    override fun getItemCount(): Int {
        return list.count()
    }

    inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        fun bind(item: Room) {
            val rangeName = itemView.findViewById<TextView>(R.id.range_name)
            rangeName.text = item.name
            val moduleRecyclerView = itemView.findViewById<ListView>(R.id.range_list_view)
            val adapter = RangeAdapter(itemView.context, rangeList)
            adapter.notifyDataSetChanged()
            moduleRecyclerView.adapter = adapter
        }

    }

}